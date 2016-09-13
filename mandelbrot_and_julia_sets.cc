#include <chrono>
#include <cmath>
#include <iostream>
#include <string>
#include <thread>
#include <memory>

#include "SDL.h"

#include "sdl_wrapper.h"

void draw_mandlebrot_set(unsigned char *screen, const double low_x, const double low_y, const double x_inc, const double y_inc, 
    const int max_iter, const int x_res, const int y_res)
{
    for (int i = 0; i < x_res; ++i)
    {
        for (int j = 0; j < y_res; ++j)
        {
            const double c_re = low_x + static_cast<double>(i) * x_inc;
            const double c_im = low_y + static_cast<double>(j) * y_inc;

            int k = max_iter;
            double z_re = c_re;
            double z_im = c_im;
            while ((--k > 0) && (((z_re * z_re) - (z_im * z_im)) < 4.0))
            {
                const double z_re_tmp = (z_re * z_re) - (z_im * z_im) + c_re;
                const double z_im_tmp = (2.0 * z_re * z_im) + c_im;

                z_re = z_re_tmp;
                z_im = z_im_tmp;
            }

            const int idx = ((j * x_res) + i) * 3;
            const double level = static_cast<double>(k) / max_iter;
            screen[idx    ] = 0;
            screen[idx + 1] = 0;
            screen[idx + 2] = static_cast<unsigned char>(level * 255.0);
        }
    }
}


void draw_julia_set(unsigned char *screen, const double c_re, const double c_im, const int max_iter, const int x_res, const int y_res)
{
    /* Auto scale */
    const double magn_c = sqrt((c_re * c_re) - (c_im * c_im));
    const double limit = (1.0 + sqrt(1.0 + (4.0 * magn_c))) * 0.5;
    const double low_x = -limit;
    const double low_y = -limit;
    const double x_inc = (2.0 * limit) / x_res;
    const double y_inc = (2.0 * limit) / y_res;

    const double limit_sq = limit * limit;
    for (int i = 0; i < x_res; ++i)
    {
        for (int j = 0; j < y_res; ++j)
        {
            int k = max_iter;
            double z_re = low_x + static_cast<double>(i) * x_inc;
            double z_im = low_y + static_cast<double>(j) * y_inc;
            while ((--k > 0) && (((z_re * z_re) + (z_im * z_im)) < limit_sq))
            {
                const double z_re_tmp = (z_re * z_re) - (z_im * z_im) + c_re;
                const double z_im_tmp = (2.0 * z_re * z_im) + c_im;

                z_re = z_re_tmp;
                z_im = z_im_tmp;
            }

            const int idx = ((j * x_res) + i) * 3;
            const double level = static_cast<double>(k) / max_iter;
            std::cout << level << std::endl;

            screen[idx    ] = 0;
            screen[idx + 1] = 0;
            screen[idx + 2] = static_cast<unsigned char>(level * 255.0);
        }
    }
}


int main()
{
    const int max_iter = 1000;

    const int x_res = 640;
    const int y_res = 480;
    const double low_x = -0.1;
    const double low_y = -0.1;
    const double hi_x =   0.1;
    const double hi_y =   0.1;
    const double x_inc = (hi_x - low_x) / x_res;
    const double y_inc = (hi_y - low_y) / y_res;

    SDL_Surface *screen;
    if (sdl_set_up(&screen, "Mandlebrot and Julia set Explorer", x_res, y_res))
    {
        return 1;
    }

    std::unique_ptr<unsigned char []> screen_data(new unsigned char [x_res * y_res * 3]);
    //draw_mandlebrot_set(screen_data.get(), low_x, low_y, x_inc, y_inc, max_iter, x_res, y_res);
    draw_julia_set(screen_data.get(), -0.8075, -0.8075, max_iter, x_res, y_res);

    if(draw_screen(screen, screen_data.get()))
    {
        return 1;
    }

    std::chrono::milliseconds dura( 1000 );
    std::this_thread::sleep_for( dura );

    /* Clean up */
    sdl_clean_up(screen, nullptr);

    return 0;
}