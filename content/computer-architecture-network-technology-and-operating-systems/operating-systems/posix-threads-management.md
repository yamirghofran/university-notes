---
title: POSIX Threads Management
---

## Mutexes
A mutex (mutual exclusion) is a lock that allows only one thread to access a resource or critical section at a time, preventing race conditions.
### Key Functions
- `pthread_mutex_init()`: Initializes a mutex.
- `pthread_mutex_lock()`: Lock a mutex. If the mutex is already locked, the calling thread is blocked until the mutex becomes available.
- `pthread_mutex_unlock()`: Unlock a mutex, potentially allowing other threds waiting for the mutex to proceed.
- `pthread_mutex_destroy()`: Destroy a mutex.
## Condition Variables
Condition variables allow threads to wait for certain conditions to occur within a program, **avoiding busy waiting**.
### Key Functions
- `pthread_cond_init()`: Initialize a condition variable.
- `pthread_cond_wait()`: Block waiting for a condition to be signaled. This function is used in conjunction with a mutex to avoid a race condition.
- `pthread_cond_signal()`: Wake up one thread waiting for the condition variable.
- `pthread_cond_broadcast()`: Wake up all threads waiting for the condition variable.
- `pthread_cond_destory()`: Destroy a condition variable.

## Read/Write Locks
Read/Write locks allow multiple threads to read a shared resource concurrently but require exclusive access for writing.
### Key Functions
- `pthread_rwlock_init()`: Initialize a read/write lock.
- `pthread_rwlock_rdlock()`: Obtain a read lock on a read/write lock.
- `pthread_rwlock_wrlock()`: Obtain a write lock on a read/write lock.
- `pthread_rwlock_unlock()`: Release either a read or write lock.
- `pthread_rwlock_destroy()`: Destroy a read/write lock.
## Semaphores
Semaphores are a lower-level synchronization mechanism that can be used for controlling access to shared resources. They are not part of pthreads, but are available in Unix/Linux systems via other libraries (POSIX semaphores).
- `sem_init()`: Initialize an unnamed semaphore.
- `sem_wait()`: Decrease the semaphore value. If it's zero, the calling thread is blocked.
- `sem_post()`: Increase the semaphore value, potentially waking up a waiting thread.
- `sem_destroy()`: Destroy the semaphore.
## Barriers
A barrier synchronizes a specific number of threads, making them all wait until each thread has reached the barrier point before any of them can proceed.
### Key Functions
- `pthread_barrier_init()`: Initialize a barrier.
- `pthread_barrier_wait()`: Wait at a barrier until the specified number of threads have called `pthread_barrier_wait()`.
- `pthread_barrier_destroy()`: Destroy a barrier.

![](../attachments/cleanshot-2025-03-13-at-1722542x.png)