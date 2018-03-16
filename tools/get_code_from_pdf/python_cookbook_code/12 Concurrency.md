```python

CHAPTER 12


Concurrency


# Code to execute in an independent thread
import time
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


# Create and launch a thread
from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()


if t.is_alive():
    print('Still running')
else:
    print('Completed')


    t.join()


t = Thread(target=countdown, args=(10,), daemon=True)
t.start()


class CountdownTask:
    def __init__(self):
        self._running = True


    def terminate(self):
        self._running = False


    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)


c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
...
c.terminate() # Signal termination
t.join()      # Wait for actual termination (if needed)


class IOTask:
    def terminate(self):
        self._running = False


    def run(self, sock):
        # sock is a socket
        sock.settimeout(5)        # Set timeout period
        while self._running:
            # Perform a blocking I/O operation w/ timeout
            try:
                data = sock.recv(8192)
                break
            except socket.timeout:
                continue
            # Continued processing
            ...
        # Terminated
        return


from threading import Thread


class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = 0
    def run(self):
        while self.n > 0:


            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)


c = CountdownThread(5)
c.start()


import multiprocessing
c = CountdownTask(5)
p = multiprocessing.Process(target=c.run)
p.start()
...


from threading import Thread, Event
import time


# Code to execute in an independent thread
def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


# Create the event object that will be used to signal startup
started_evt = Event()


# Launch the thread and pass the startup event
print('Launching countdown')
t = Thread(target=countdown, args=(10,started_evt))
t.start()


# Wait for the thread to start
started_evt.wait()
print('countdown is running')


import threading
import time


class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()


    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True


        t.start()


    def run(self):
        '''
        Run the timer and notify waiting threads after each interval
        '''
        while True:
            time.sleep(self._interval)
            with self._cv:
                 self._flag ^= 1
                 self._cv.notify_all()


    def wait_for_tick(self):
        '''
        Wait for the next tick of the timer
        '''
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()


# Example use of the timer
ptimer = PeriodicTimer(5)
ptimer.start()


# Two threads that synchronize on the timer
def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print('T-minus', nticks)
        nticks -= 1


def countup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print('Counting', n)
        n += 1


threading.Thread(target=countdown, args=(10,)).start()
threading.Thread(target=countup, args=(5,)).start()


# Worker thread
def worker(n, sema):
    # Wait to be signaled
    sema.acquire()


    # Do some work
    print('Working', n)


# Create some threads
sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema,))
    t.start()


>>> sema.release()
Working 0
>>> sema.release()
Working 1
>>>


from queue import Queue
from threading import Thread


# A thread that produces data
def producer(out_q):
    while True:
        # Produce some data
        ...
        out_q.put(data)


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        # Process the data
        ...


# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()


from queue import Queue
from threading import Thread


# Object that signals shutdown
_sentinel = object()


# A thread that produces data
def producer(out_q):
    while running:
        # Produce some data
        ...
        out_q.put(data)


    # Put the sentinel on the queue to indicate completion
    out_q.put(_sentinel)


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()


        # Check for termination
        if data is _sentinel:
            in_q.put(_sentinel)
            break


        # Process the data
        ...


import heapq
import threading


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()
    def put(self, item, priority):
        with self._cv:
            heapq.heappush(self._queue, (-priority, self._count, item))
            self._count += 1
            self._cv.notify()


    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()
            return heapq.heappop(self._queue)[-1]


from queue import Queue
from threading import Thread


# A thread that produces data
def producer(out_q):
    while running:
        # Produce some data
        ...
        out_q.put(data)


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()


        # Process the data
        ...
        # Indicate completion
        in_q.task_done()


# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()


# Wait for all produced items to be consumed
q.join()


from queue import Queue
from threading import Thread, Event


# A thread that produces data
def producer(out_q):
    while running:
        # Produce some data
        ...
        # Make an (data, event) pair and hand it to the consumer
        evt = Event()
        out_q.put((data, evt))
        ...
        # Wait for the consumer to process the item
        evt.wait()


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data, evt = in_q.get()
        # Process the data
        ...
        # Indicate completion
        evt.set()


from queue import Queue
from threading import Thread
import copy


# A thread that produces data
def producer(out_q):
    while True:
        # Produce some data
        ...
        out_q.put(copy.deepcopy(data))


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        # Process the data
        ...


import queue
q = queue.Queue()


try:
    data = q.get(block=False)
except queue.Empty:
    ...


try:
    q.put(item, block=False)
except queue.Full:
    ...


try:
    data = q.get(timeout=5.0)
except queue.Empty:
    ...


def producer(q):
    ...
    try:
        q.put(item, block=False)
    except queue.Full:
        log.warning('queued item %r discarded!', item)


_running = True


def consumer(q):
    while _running:
        try:
            item = q.get(timeout=5.0)
            # Process item
            ...
        except queue.Empty:
            pass


import threading


class SharedCounter:
    '''
    A counter object that can be shared by multiple threads.
    '''
    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._value_lock = threading.Lock()


    def incr(self,delta=1):
        '''
        Increment the counter with locking
        '''
        with self._value_lock:
             self._value += delta


    def decr(self,delta=1):
        '''
        Decrement the counter with locking
        '''
        with self._value_lock:
             self._value -= delta


import threading


class SharedCounter:
    '''
    A counter object that can be shared by multiple threads.
    '''
    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._value_lock = threading.Lock()


    def incr(self,delta=1):
        '''
        Increment the counter with locking
        '''
        self._value_lock.acquire()
        self._value += delta
        self._value_lock.release()


    def decr(self,delta=1):
        '''
        Decrement the counter with locking
        '''
        self._value_lock.acquire()
        self._value -= delta
        self._value_lock.release()


import threading


class SharedCounter:
    '''
    A counter object that can be shared by multiple threads.
    '''
    _lock = threading.RLock()
    def __init__(self, initial_value = 0):
        self._value = initial_value


    def incr(self,delta=1):
        '''
        Increment the counter with locking
        '''
        with SharedCounter._lock:
            self._value += delta


    def decr(self,delta=1):
        '''
        Decrement the counter with locking
        '''
        with SharedCounter._lock:
             self.incr(-delta)


from threading import Semaphore
import urllib.request


# At most, five threads allowed to run at once
_fetch_url_sema = Semaphore(5)


def fetch_url(url):
    with _fetch_url_sema:
        return urllib.request.urlopen(url)


import threading
from contextlib import contextmanager


# Thread-local state to stored information on locks already acquired
_local = threading.local()


@contextmanager
def acquire(*locks):
    # Sort locks by object identifier
    locks = sorted(locks, key=lambda x: id(x))


    # Make sure lock order of previously acquired locks is not violated
    acquired = getattr(_local,'acquired',[])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')


    # Acquire all of the locks
    acquired.extend(locks)
    _local.acquired = acquired


    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # Release locks in reverse order of acquisition
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


import threading
x_lock = threading.Lock()
y_lock = threading.Lock()


def thread_1():
    while True:
        with acquire(x_lock, y_lock):
            print('Thread-1')


def thread_2():
    while True:
        with acquire(y_lock, x_lock):
            print('Thread-2')


t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()


t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()


import threading
x_lock = threading.Lock()
y_lock = threading.Lock()


def thread_1():


    while True:
        with acquire(x_lock):
            with acquire(y_lock):
                print('Thread-1')


def thread_2():
    while True:
        with acquire(y_lock):
            with acquire(x_lock):
                print('Thread-2')


t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()


t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()


Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/local/lib/python3.3/threading.py", line 639, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.3/threading.py", line 596, in run
    self._target(*self._args, **self._kwargs)
  File "deadlock.py", line 49, in thread_1
    with acquire(y_lock):
  File "/usr/local/lib/python3.3/contextlib.py", line 48, in __enter__
    return next(self.gen)
  File "deadlock.py", line 15, in acquire
    raise RuntimeError("Lock Order Violation")
RuntimeError: Lock Order Violation
>>>


import threading


# The philosopher thread
def philosopher(left, right):
    while True:
        with acquire(left,right):
             print(threading.currentThread(), 'eating')


# The chopsticks (represented by locks)
NSTICKS = 5
chopsticks = [threading.Lock() for n in range(NSTICKS)]


# Create all of the philosophers
for n in range(NSTICKS):
    t = threading.Thread(target=philosopher,
                         args=(chopsticks[n],chopsticks[(n+1) % NSTICKS]))
    t.start()


from socket import socket, AF_INET, SOCK_STREAM
import threading


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.local = threading.local()


    def __enter__(self):
        if hasattr(self.local, 'sock'):
            raise RuntimeError('Already connected')
        self.local.sock = socket(self.family, self.type)
        self.local.sock.connect(self.address)
        return self.local.sock


    def __exit__(self, exc_ty, exc_val, tb):
        self.local.sock.close()
        del self.local.sock


from functools import partial
def test(conn):
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')


        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))


    print('Got {} bytes'.format(len(resp)))


if __name__ == '__main__':
    conn = LazyConnection(('www.python.org', 80))


    t1 = threading.Thread(target=test, args=(conn,))
    t2 = threading.Thread(target=test, args=(conn,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


from socket import AF_INET, SOCK_STREAM, socket
from concurrent.futures import ThreadPoolExecutor


def echo_client(sock, client_addr):
    '''
    Handle a client connection
    '''
    print('Got connection from', client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('Client closed connection')
    sock.close()


def echo_server(addr):
    pool = ThreadPoolExecutor(128)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client, client_sock, client_addr)


echo_server(('',15000))


from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from queue import Queue


def echo_client(q):
    '''
    Handle a client connection
    '''
    sock, client_addr = q.get()
    print('Got connection from', client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('Client closed connection')


    sock.close()


def echo_server(addr, nworkers):
    # Launch the client workers
    q = Queue()
    for n in range(nworkers):
        t = Thread(target=echo_client, args=(q,))
        t.daemon = True
        t.start()


    # Run the server
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        q.put((client_sock, client_addr))


echo_server(('',15000), 128)


from concurrent.futures import ThreadPoolExecutor
import urllib.request


def fetch_url(url):
    u = urllib.request.urlopen(url)
    data = u.read()
    return data


pool = ThreadPoolExecutor(10)
# Submit work to the pool
a = pool.submit(fetch_url, 'http://www.python.org')
b = pool.submit(fetch_url, 'http://www.pypy.org')


# Get the results back
x = a.result()
y = b.result()


from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM


def echo_client(sock, client_addr):
    '''
    Handle a client connection
    '''
    print('Got connection from', client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('Client closed connection')
    sock.close()


def echo_server(addr, nworkers):
    # Run the server
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        t = Thread(target=echo_client, args=(client_sock, client_addr))
        t.daemon = True
        t.start()


echo_server(('',15000))


import threading
threading.stack_size(65536)


logs/
   20120701.log.gz
   20120702.log.gz
   20120703.log.gz
   20120704.log.gz
   20120705.log.gz
   20120706.log.gz
   ...


124.115.6.12 - - [10/Jul/2012:00:18:50 -0500] "GET /robots.txt ..." 200 71
210.212.209.67 - - [10/Jul/2012:00:18:51 -0500] "GET /ply/ ..." 200 11875
210.212.209.67 - - [10/Jul/2012:00:18:51 -0500] "GET /favicon.ico ..." 404 369
61.135.216.105 - - [10/Jul/2012:00:20:04 -0500] "GET /blog/atom.xml ..." 304 -
...


# findrobots.py


import gzip
import io
import glob


def find_robots(filename):
    '''
    Find all of the hosts that access robots.txt in a single log file
    '''
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f,encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots


def find_all_robots(logdir):
    '''
    Find all hosts across and entire sequence of files
    '''
    files = glob.glob(logdir+'/*.log.gz')
    all_robots = set()
    for robots in map(find_robots, files):
        all_robots.update(robots)
    return all_robots


if __name__ == '__main__':
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)


# findrobots.py


import gzip
import io
import glob
from concurrent import futures


def find_robots(filename):
    '''
    Find all of the hosts that access robots.txt in a single log file


    '''
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f,encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots


def find_all_robots(logdir):
    '''
    Find all hosts across and entire sequence of files
    '''
    files = glob.glob(logdir+'/*.log.gz')
    all_robots = set()
    with futures.ProcessPoolExecutor() as pool:
        for robots in pool.map(find_robots, files):
            all_robots.update(robots)
    return all_robots


if __name__ == '__main__':
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)


from concurrent.futures import ProcessPoolExecutor


with ProcessPoolExecutor() as pool:
    ...
    do work in parallel using pool
    ...


# A function that performs a lot of work
def work(x):
    ...
    return result


# Nonparallel code
results = map(work, data)


# Parallel implementation
with ProcessPoolExecutor() as pool:
    results = pool.map(work, data)


# Some function
def work(x):
    ...
    return result


with ProcessPoolExecutor() as pool:
    ...
    # Example of submitting work to the pool
    future_result = pool.submit(work, arg)


    # Obtaining the result (blocks until done)
    r = future_result.result()
    ...


def when_done(r):
    print('Got:', r.result())


with ProcessPoolExecutor() as pool:
     future_result = pool.submit(work, arg)
     future_result.add_done_callback(when_done)


• This technique for parallelization only works well for problems that can be trivially
decomposed into independent parts.


• Work must be submitted in the form of simple functions. Parallel execution of
instance methods, closures, or other kinds of constructs are not supported.
• Function arguments and return values must be compatible with pickle. Work is
carried out in a separate interpreter using interprocess communication. Thus, data
exchanged between interpreters has to be serialized.
• Functions submitted for work should not maintain persistent state or have side
effects. With the exception of simple things such as logging, you don’t really have
any control over the behavior of child processes once started. Thus, to preserve your
sanity, it is probably best to keep things simple and carry out work in pure-functions
that don’t alter their environment.
• Process pools are created by calling the fork() system call on Unix. This makes a
clone of the Python interpreter, including all of the program state at the time of the
fork. On Windows, an independent copy of the interpreter that does not clone state
is launched. The actual forking process does not occur until the first pool.map()
or pool.submit() method is called.
• Great care should be made when combining process pools and programs that use
threads. In particular, you should probably create and launch process pools prior
to the creation of any threads (e.g., create the pool in the main thread at program
startup).


# Performs a large calculation (CPU bound)
def some_work(args):
    ...
    return result


# A thread that calls the above function
def some_thread():
    while True:
        ...
        r = some_work(args)
        ...


# Processing pool (see below for initiazation)
pool = None


# Performs a large calculation (CPU bound)
def some_work(args):
    ...
    return result


# A thread that calls the above function
def some_thread():
    while True:
        ...
        r = pool.apply(some_work, (args))
        ...


# Initiaze the pool
if __name__ == '__main__':
    import multiprocessing
    pool = multiprocessing.Pool()


#include "Python.h"
...


PyObject *pyfunc(PyObject *self, PyObject *args) {
   ...
   Py_BEGIN_ALLOW_THREADS
   // Threaded C code
   ...
   Py_END_ALLOW_THREADS
   ...
}


from queue import Queue
from threading import Thread, Event


# Sentinel used for shutdown
class ActorExit(Exception):
    pass


class Actor:
    def __init__(self):
        self._mailbox = Queue()


    def send(self, msg):
        '''
        Send a message to the actor
        '''
        self._mailbox.put(msg)


    def recv(self):
        '''
        Receive an incoming message
        '''
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg


    def close(self):
        '''
        Close the actor, thus shutting it down
        '''
        self.send(ActorExit)


    def start(self):
        '''
        Start concurrent execution
        '''
        self._terminated = Event()
        t = Thread(target=self._bootstrap)


        t.daemon = True
        t.start()


    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()


    def join(self):
        self._terminated.wait()


    def run(self):
        '''
        Run method to be implemented by the user
        '''
        while True:
            msg = self.recv()


# Sample ActorTask
class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print('Got:', msg)


# Sample use
p = PrintActor()
p.start()
p.send('Hello')
p.send('World')
p.close()
p.join()


def print_actor():
    while True:


        try:
            msg = yield      # Get a message
            print('Got:', msg)
        except GeneratorExit:
            print('Actor terminating')


# Sample use
p = print_actor()
next(p)     # Advance to the yield (ready to receive)
p.send('Hello')
p.send('World')
p.close()


class TaggedActor(Actor):
    def run(self):
        while True:
             tag, *payload = self.recv()
             getattr(self,'do_'+tag)(*payload)


    # Methods correponding to different message tags
    def do_A(self, x):
        print('Running A', x)


    def do_B(self, x, y):
        print('Running B', x, y)


# Example
a = TaggedActor()
a.start()
a.send(('A', 1))      # Invokes do_A(1)
a.send(('B', 2, 3))   # Invokes do_B(2,3)


from threading import Event
class Result:
    def __init__(self):
        self._evt = Event()
        self._result = None


    def set_result(self, value):
        self._result = value


        self._evt.set()


    def result(self):
        self._evt.wait()
        return self._result


class Worker(Actor):
    def submit(self, func, *args, **kwargs):
        r = Result()
        self.send((func, args, kwargs, r))
        return r


    def run(self):
        while True:
            func, args, kwargs, r = self.recv()
            r.set_result(func(*args, **kwargs))


# Example use
worker = Worker()
worker.start()
r = worker.submit(pow, 2, 3)
print(r.result())


from collections import defaultdict


class Exchange:
    def __init__(self):
        self._subscribers = set()


    def attach(self, task):
        self._subscribers.add(task)


    def detach(self, task):
        self._subscribers.remove(task)


    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


# Dictionary of all created exchanges
_exchanges = defaultdict(Exchange)


# Return the Exchange instance associated with a given name
def get_exchange(name):
    return _exchanges[name]


# Example of a task.  Any object with a send() method


class Task:
    ...
    def send(self, msg):
        ...


task_a = Task()
task_b = Task()


# Example of getting an exchange
exc = get_exchange('name')


# Examples of subscribing tasks to it
exc.attach(task_a)
exc.attach(task_b)


# Example of sending messages
exc.send('msg1')
exc.send('msg2')


# Example of unsubscribing
exc.detach(task_a)
exc.detach(task_b)


class DisplayMessages:
    def __init__(self):
        self.count = 0
    def send(self, msg):
        self.count += 1
        print('msg[{}]: {!r}'.format(self.count, msg))


exc = get_exchange('name')
d = DisplayMessages()
exc.attach(d)


exc = get_exchange('name')
exc.attach(some_task)
try:
    ...
finally:
    exc.detach(some_task)


from contextlib import contextmanager
from collections import defaultdict


class Exchange:
    def __init__(self):
        self._subscribers = set()


    def attach(self, task):
        self._subscribers.add(task)


    def detach(self, task):
        self._subscribers.remove(task)


    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)


    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


# Dictionary of all created exchanges
_exchanges = defaultdict(Exchange)


# Return the Exchange instance associated with a given name
def get_exchange(name):
    return _exchanges[name]


# Example of using the subscribe() method
exc = get_exchange('name')
with exc.subscribe(task_a, task_b):
     ...
     exc.send('msg1')
     exc.send('msg2')
     ...


# task_a and task_b detached here


# Two simple generator functions
def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield
        n -= 1
    print('Blastoff!')


def countup(n):
    x = 0
    while x < n:
        print('Counting up', x)
        yield
        x += 1


from collections import deque


class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()


    def new_task(self, task):
        '''
        Admit a newly started task to the scheduler


        '''
        self._task_queue.append(task)


    def run(self):
        '''
        Run until there are no more tasks
        '''
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                # Run until the next yield statement
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                # Generator is no longer executing
                pass


# Example use
sched = TaskScheduler()
sched.new_task(countdown(10))
sched.new_task(countdown(5))
sched.new_task(countup(15))
sched.run()


T-minus 10
T-minus 5
Counting up 0
T-minus 9
T-minus 4
Counting up 1
T-minus 8
T-minus 3
Counting up 2
T-minus 7
T-minus 2
...


from collections import deque


class ActorScheduler:
    def __init__(self):
        self._actors = { }          # Mapping of names to actors
        self._msg_queue = deque()   # Message queue


    def new_actor(self, name, actor):
        '''
        Admit a newly started actor to the scheduler and give it a name
        '''
        self._msg_queue.append((actor,None))
        self._actors[name] = actor


    def send(self, name, msg):
        '''
        Send a message to a named actor
        '''
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor,msg))


    def run(self):
        '''
        Run as long as there are pending messages.
        '''
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                 actor.send(msg)
            except StopIteration:
                 pass


# Example use
if __name__ == '__main__':
    def printer():
        while True:
            msg = yield
            print('Got:', msg)


    def counter(sched):
        while True:
            # Receive the current count
            n = yield
            if n == 0:
                break
            # Send to the printer task
            sched.send('printer', n)
            # Send the next count to the counter task (recursive)


            sched.send('counter', n-1)


    sched = ActorScheduler()
    # Create the initial actors
    sched.new_actor('printer', printer())
    sched.new_actor('counter', counter(sched))


    # Send an initial message to the counter to initiate
    sched.send('counter', 10000)
    sched.run()


from collections import deque
from select import select


# This class represents a generic yield event in the scheduler
class YieldEvent:
    def handle_yield(self, sched, task):
        pass
    def handle_resume(self, sched, task):
        pass


# Task Scheduler
class Scheduler:
    def __init__(self):
        self._numtasks = 0       # Total num of tasks
        self._ready = deque()    # Tasks ready to run
        self._read_waiting = {}  # Tasks waiting to read
        self._write_waiting = {} # Tasks waiting to write


    # Poll for I/O events and restart waiting tasks
    def _iopoll(self):
        rset,wset,eset = select(self._read_waiting,
                                self._write_waiting,[])
        for r in rset:
            evt, task = self._read_waiting.pop(r)
            evt.handle_resume(self, task)
        for w in wset:
            evt, task = self._write_waiting.pop(w)
            evt.handle_resume(self, task)


    def new(self,task):
        '''
        Add a newly started task to the scheduler
        '''


        self._ready.append((task, None))
        self._numtasks += 1


    def add_ready(self, task, msg=None):
        '''
        Append an already started task to the ready queue.
        msg is what to send into the task when it resumes.
        '''
        self._ready.append((task, msg))


    # Add a task to the reading set
    def _read_wait(self, fileno, evt, task):
        self._read_waiting[fileno] = (evt, task)


    # Add a task to the write set
    def _write_wait(self, fileno, evt, task):
        self._write_waiting[fileno] = (evt, task)


    def run(self):
        '''
        Run the task scheduler until there are no tasks
        '''
        while self._numtasks:
             if not self._ready:
                  self._iopoll()
             task, msg = self._ready.popleft()
             try:
                 # Run the coroutine to the next yield
                 r = task.send(msg)
                 if isinstance(r, YieldEvent):
                     r.handle_yield(self, task)
                 else:
                     raise RuntimeError('unrecognized yield event')
             except StopIteration:
                 self._numtasks -= 1


# Example implementation of coroutine-based socket I/O
class ReadSocket(YieldEvent):
    def __init__(self, sock, nbytes):
        self.sock = sock
        self.nbytes = nbytes
    def handle_yield(self, sched, task):
        sched._read_wait(self.sock.fileno(), self, task)
    def handle_resume(self, sched, task):
        data = self.sock.recv(self.nbytes)
        sched.add_ready(task, data)


class WriteSocket(YieldEvent):
    def __init__(self, sock, data):
        self.sock = sock
        self.data = data
    def handle_yield(self, sched, task):


        sched._write_wait(self.sock.fileno(), self, task)
    def handle_resume(self, sched, task):
        nsent = self.sock.send(self.data)
        sched.add_ready(task, nsent)


class AcceptSocket(YieldEvent):
    def __init__(self, sock):
        self.sock = sock
    def handle_yield(self, sched, task):
        sched._read_wait(self.sock.fileno(), self, task)
    def handle_resume(self, sched, task):
        r = self.sock.accept()
        sched.add_ready(task, r)


# Wrapper around a socket object for use with yield
class Socket(object):
    def __init__(self, sock):
        self._sock = sock
    def recv(self, maxbytes):
        return ReadSocket(self._sock, maxbytes)
    def send(self, data):
        return WriteSocket(self._sock, data)
    def accept(self):
        return AcceptSocket(self._sock)
    def __getattr__(self, name):
        return getattr(self._sock, name)


if __name__ == '__main__':
    from socket import socket, AF_INET, SOCK_STREAM
    import time


    # Example of a function involving generators.  This should
    # be called using line = yield from readline(sock)
    def readline(sock):
        chars = []
        while True:
            c = yield sock.recv(1)
            if not c:
                break
            chars.append(c)
            if c == b'\n':
                break
        return b''.join(chars)


    # Echo server using generators
    class EchoServer:
        def __init__(self,addr,sched):
            self.sched = sched
            sched.new(self.server_loop(addr))


        def server_loop(self,addr):
            s = Socket(socket(AF_INET,SOCK_STREAM))


            s.bind(addr)
            s.listen(5)
            while True:
                c,a = yield s.accept()
                print('Got connection from ', a)
                self.sched.new(self.client_handler(Socket(c)))


        def client_handler(self,client):
            while True:
                line = yield from readline(client)
                if not line:
                    break
                line = b'GOT:' + line
                while line:
                    nsent = yield client.send(line)
                    line = line[nsent:]
            client.close()
            print('Client closed')


    sched = Scheduler()
    EchoServer(('',16000),sched)
    sched.run()


def some_generator():
    ...
    result = yield data
    ...


f = some_generator()


# Initial result. Is None to start since nothing has been computed
result = None
while True:
    try:
        data = f.send(result)
        result = ... do some calculation ...
    except StopIteration:
        break


import queue
import socket
import os


class PollableQueue(queue.Queue):
    def __init__(self):
        super().__init__()
        # Create a pair of connected sockets
        if os.name == 'posix':
            self._putsocket, self._getsocket = socket.socketpair()
        else:
            # Compatibility on non-POSIX systems
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('127.0.0.1', 0))
            server.listen(1)
            self._putsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._putsocket.connect(server.getsockname())
            self._getsocket, _ = server.accept()
            server.close()


    def fileno(self):
        return self._getsocket.fileno()


    def put(self, item):
        super().put(item)
        self._putsocket.send(b'x')


    def get(self):
        self._getsocket.recv(1)
        return super().get()


import select
import threading


def consumer(queues):
    '''
    Consumer that reads data on multiple queues simultaneously
    '''
    while True:
        can_read, _, _ = select.select(queues,[],[])
        for r in can_read:
            item = r.get()
            print('Got:', item)


q1 = PollableQueue()
q2 = PollableQueue()
q3 = PollableQueue()
t = threading.Thread(target=consumer, args=([q1,q2,q3],))
t.daemon = True
t.start()


# Feed data to the queues
q1.put(1)
q2.put(10)
q3.put('hello')
q2.put(15)
...


import time
def consumer(queues):
    while True:
        for q in queues:
            if not q.empty():
                item = q.get()
                print('Got:', item)


        # Sleep briefly to avoid 100% CPU
        time.sleep(0.01)


import select


def event_loop(sockets, queues):
    while True:
        # polling with a timeout
        can_read, _, _ = select.select(sockets, [], [], 0.01)
        for r in can_read:
            handle_read(r)
        for q in queues:
            if not q.empty():
                item = q.get()
                print('Got:', item)


#!/usr/bin/env python3
# daemon.py


import os
import sys


import atexit
import signal


def daemonize(pidfile, *, stdin='/dev/null',
                          stdout='/dev/null',
                          stderr='/dev/null'):


    if os.path.exists(pidfile):
        raise RuntimeError('Already running')


    # First fork (detaches from parent)
    try:
        if os.fork() > 0:
            raise SystemExit(0)   # Parent exit
    except OSError as e:
        raise RuntimeError('fork #1 failed.')


    os.chdir('/')
    os.umask(0)
    os.setsid()
    # Second fork (relinquish session leadership)
    try:
        if os.fork() > 0:
            raise SystemExit(0)
    except OSError as e:
        raise RuntimeError('fork #2 failed.')


    # Flush I/O buffers
    sys.stdout.flush()
    sys.stderr.flush()


    # Replace file descriptors for stdin, stdout, and stderr
    with open(stdin, 'rb', 0) as f:
        os.dup2(f.fileno(), sys.stdin.fileno())
    with open(stdout, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stdout.fileno())
    with open(stderr, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stderr.fileno())


    # Write the PID file
    with open(pidfile,'w') as f:
        print(os.getpid(),file=f)


    # Arrange to have the PID file removed on exit/signal
    atexit.register(lambda: os.remove(pidfile))


    # Signal handler for termination (required)
    def sigterm_handler(signo, frame):
        raise SystemExit(1)


    signal.signal(signal.SIGTERM, sigterm_handler)


def main():
    import time
    sys.stdout.write('Daemon started with pid {}\n'.format(os.getpid()))
    while True:
        sys.stdout.write('Daemon Alive! {}\n'.format(time.ctime()))
        time.sleep(10)


if __name__ == '__main__':
    PIDFILE = '/tmp/daemon.pid'


    if len(sys.argv) != 2:
        print('Usage: {} [start|stop]'.format(sys.argv[0]), file=sys.stderr)
        raise SystemExit(1)


    if sys.argv[1] == 'start':
        try:
            daemonize(PIDFILE,
                      stdout='/tmp/daemon.log',
                      stderr='/tmp/dameon.log')
        except RuntimeError as e:
            print(e, file=sys.stderr)
            raise SystemExit(1)


        main()


    elif sys.argv[1] == 'stop':
        if os.path.exists(PIDFILE):
            with open(PIDFILE) as f:
                os.kill(int(f.read()), signal.SIGTERM)
        else:
            print('Not running', file=sys.stderr)
            raise SystemExit(1)


    else:
        print('Unknown command {!r}'.format(sys.argv[1]), file=sys.stderr)
        raise SystemExit(1)


bash % daemon.py start
bash % cat /tmp/daemon.pid
2882
bash % tail -f /tmp/daemon.log
Daemon started with pid 2882
Daemon Alive! Fri Oct 12 13:45:37 2012
Daemon Alive! Fri Oct 12 13:45:47 2012
...


bash % daemon.py stop
bash %


daemonize('daemon.pid',
          stdin='/dev/null,
          stdout='/tmp/daemon.log',
          stderr='/tmp/daemon.log')


# Illegal. Must use keyword arguments
daemonize('daemon.pid',
          '/dev/null', '/tmp/daemon.log','/tmp/daemon.log')
```