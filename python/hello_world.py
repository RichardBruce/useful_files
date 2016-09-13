import math
import sys
import turtle

#print({ r : math.exp(10.0 * float(r)) for r in sys.argv[1:]})

#try :
#	f = open(sys.argv[1], 'r')
#except IOError:
#	print ('Could not open file {}'.format(sys.argv[1]))
#	exit()
#
#chars = 0
#words = 0
#lines = 0
#for line in f:
#	lines += 1
#	for word in line.split(' '):
#		words += 1
#		chars += len(word)
#		print (word)
#
#print ("File contains {0} lines, {1} words and {2} characters".format(lines, words, chars))
#f.close()

#def is_prime(possible):
#	for i in range(possible) :
#		for j in range(possible) :
#			mult = i * j
#			if mult == possible :
#				return False
#			#elif mult > possible :
#				#break
#	return True
#	
#def primes_between(begin, end) :
#	return [i for i in range(begin, end) if is_prime(i)]
#	
#print (primes_between(0, 30))
			
#def iterative_factorial(n) :
#	fac = 1
#	for i in range(1, n + 1) :
#		fac *= i
#		
#	return fac
#	
#def recursive_factorial(n) :
#	if (n == 0) or (n == 1) :
#		return 1
#	else :
#		return n * recursive_factorial(n - 1)
#	
#if __name__ == '__main__' :
#	print ('Iterative factorial gives: {}'.format(iterative_factorial(int(sys.argv[1]))))
#	print ('Recursive factorial gives: {}'.format(recursive_factorial(int(sys.argv[1]))))


#def recursive_factorial(n) :
#	if n < 2 :
#		return 1
#	else :
#		return n * recursive_factorial(n - 1)
#	
#if __name__ == '__main__' :
#	import unittest
#	class factorial_test(unittest.TestCase) :
#		def test_zero(self) :
#			self.assertEqual(1, recursive_factorial(0))
#			
#		def test_one(self) :
#			self.assertEqual(1, recursive_factorial(1))
#			
#		def test_two(self) :
#			self.assertEqual(2, recursive_factorial(2))
#			
#		def test_three(self) :
#			self.assertEqual(6, recursive_factorial(3))
#			
#		def test_many(self) :
#			self.assertEqual(30414093201713378043612608166064768844377641568960512000000000000, recursive_factorial(50))
#	
#	unittest.main()

#import time
#import multiprocessing
#import threading
#
#def countdown_sequential(identity, count):
#	for i in range(count):
#		for j in range(10000000):
#			pass
#		print('{} {} {}'.format(identity, i, time.time()))
#		
#def countdown_process(identity, count, queue):
#	for i in range(count):
#		for j in range(10000000):
#			pass
#		print('{} {} {}'.format(identity, i, time.time()))
#	queue.put(i)
#
#
#if __name__ == '__main__':
#	startTime = time.time()
#	for i in range(8):
#		countdown_sequential(i, 5)
#	print('Elapse time = {}'.format(time.time() - startTime))
#	
#	startTime = time.time()
#	threads = [threading.Thread(target=countdown_sequential, args=(i, 5)) for i in range (8)]
#	for thread in threads:
#		thread.start()
#		
#	for thread in threads :
#		thread.join()
#	print('Elapse time = {}'.format(time.time() - startTime))
#
#	startTime = time.time()	
#	result_queue = multiprocessing.Queue()
#	processes = [multiprocessing.Process(target=countdown_sequential, args=(i, 5)) for i in range (8)]
#	for process in processes :
#		process.start()
#	for process in processes :
#		process.join()
#	print('Elapse time = {}'.format(time.time() - startTime))
#	
#from sqlalchemy import *
#
#if __name__ == '__main__' :
#	db = create_engine('sqlite:///test.db')
#	
#	metadata = BoundMetaData(db)
#
#	users = Table('users', metadata,
#		Column('user_id', Integer, primary_key=True),
#		Column('name', String(40)),
#		Column('age', Integer),
#		Column('password', String),
#	)
#	users.create()

from ctypes import *
cdll.LoadLibrary("libjpeg.so") 
cdll.LoadLibrary("libraytracer.so") 
