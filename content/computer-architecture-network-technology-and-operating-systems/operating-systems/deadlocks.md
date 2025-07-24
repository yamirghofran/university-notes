---
title: Deadlocks
---

![](../attachments/cleanshot-2025-02-21-at-1615122x.png)
## Conditions for Deadlock
- Mutual exclusion
	- At least one resource must be held in a non-shareable mode →  only one thread at a time can use the resource.
- Hold and wait
	- A thread must be holding at least one resource and waiting to acquire additional resources that are currently being held by other threads.
- No preemtion
	- Resources cannot be forcibly removed from the threads holding them; threads must release resources voluntarily.
- Circular wait
	- There exists a set of waiting processes {P1, P2, ..., Pn} such that P1 is waiting for a resource held by P2, P2 is waiting for a resource held by P3,..., and Pn is waiting for a resource held by P1, forming a cycle.

## Common Scenarios
- Resource Allocation Deadlocks
	- When multiple threads attempt to lock multiple resources without a consistent ordering, they may end up waiting on each other to release the locks.
- Database Transactions
	- Deadlocks can occur in databases when different transactions lock rows of tables in incompatible orders and then each transaction waits for the other to release its lock
- Thread Synchronization
	- Incorrect use of synchronization primitives (like mutexes, semaphores, or condition variables) can lead to situations where threads wait indefinitely for signals or resources held by each other.

## Prevention and Mitigation
- Avoiding Hold and Wait
	- Design the system so that a thread requests all required resources at once, reducing the chance of waiting while holding resources.
- Resource Ordering
	- Establish a global order in which resources are requested by all threads. This prevents circular wait conditions.
- Lock Timeout
	- Use lock timeouts so that if a thread cannot acquire all its needed resources within a certain timeframe, it releases any locks it holds and retries later.
- Deadlock Detection
	- Implement deadlock detection algorithms that periodically check for cycles of resource allocation graphs. If a deadlock is detected, one or more threads can be preempted to break the cycle.
- Preemption and Resource Repossession
	- In some cases, preempting resources from a thread (if possible) and reallocating them to break the deadlock cycle can be a solution, though this may not be feasible or safe for all types of resources.

**Advanced**
- Resource Allocation Graph (RAG)
![](../attachments/cleanshot-2025-02-27-at-1042362x.png)
- Banker's Algorithm. (research how to implement on your own)
	- Replicates how a bank works.
	- How much of each resource each process could possibly request ("MAX")
	- How much of each resource each process is currently holding ("ALLOCATED")
	- How much of each resource the system currently has available ("AVAILABLE")
	
```python
	def banker_algorithm(available, max_resources, allocation):
    """
    Banker's algorithm to detect deadlock.
    
    Parameters:
    available (list): Available resources.
    max_resources (list of lists): Maximum resources for each process.
    allocation (list of lists): Allocated resources for each process.
    
    Returns:
    bool: True if the system is safe, False otherwise.
    """
    # Calculate the need for each process
    need = [[max_resources[i][j] - allocation[i][j] for j in range(len(available))] for i in range(len(max_resources))]
    
    # Initialize the finish vector
    finish = [False] * len(max_resources)
    
    # Initialize the safe sequence
    safe_sequence = []
    
    while False in finish:
        found = False
        for i in range(len(max_resources)):
            if not finish[i]:
                # Check if the need can be satisfied by the available resources
                if all(need[i][j] <= available[j] for j in range(len(available))):
                    # Allocate the resources and update the available resources
                    for j in range(len(available)):
                        available[j] += allocation[i][j]
                    # Mark the process as finished
                    finish[i] = True
                    # Add the process to the safe sequence
                    safe_sequence.append(i)
                    found = True
        if not found:
            # If no process can be finished, the system is not safe
            return False
    
    return True

# Example usage
available = [2, 3, 2]
max_resources = [[7, 5, 3], [3, 2, 2], [9, 0, 2]]
allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2]]

if banker_algorithm(available, max_resources, allocation):
    print("The system is safe.")
else:
    print("The system is not safe.")

```

### Banker's Algorithm Steps:

1. **Initialize**:
	* Create matrices for **Available**, **Max**, **Allocation**, and **Need** resources.
2. **Calculate Need**:
	* **Need** = **Max** - **Allocation** for each process.
3. **Find Safe Process**:
	* Find a process where **Need** ≤ **Available**.
4. **Allocate Resources**:
	* If a safe process is found, allocate **Need** resources to it.
	* Update **Available**, **Allocation**, and **Need** matrices.
5. **Mark Process as Finished**:
	* Mark the allocated process as finished.
6. **Repeat**:
	* Repeat steps 3-5 until all processes are finished or no safe process can be found.
7. **Check for Safety**:
	* If all processes are finished, the system is safe.
	* Otherwise, the system is not safe.

