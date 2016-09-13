# Create build dir
mkdir clang
cd clang

# Check out llvm
svn co http://llvm.org/svn/llvm-project/llvm/trunk llvm

# Check out clang
cd llvm/tools
svn co http://llvm.org/svn/llvm-project/cfe/trunk clang
cd ../..

# Check out extra clang tools
cd llvm/tools/clang/tools
svn co http://llvm.org/svn/llvm-project/clang-tools-extra/trunk extra
cd ../../../..

# Check out compiler-rt
cd llvm/projects
svn co http://llvm.org/svn/llvm-project/compiler-rt/trunk compiler-rt
cd ../..

# Build
mkdir build
cd build
../llvm/configure --enable-optimized --enable-cxx11
make -j 8
