---
title: SimPy for Discrete Events Simulation
---

- [SimPy Generators](/simulating-and-modelling-to-understand-change/module-iii---discrete-events-simulation/simpy/simpy-generators)
- [SimPy Containers](/simulating-and-modelling-to-understand-change/module-iii---discrete-events-simulation/simpy/simpy-containers)
- [SimPy Warmup](/simulating-and-modelling-to-understand-change/module-iii---discrete-events-simulation/simpy/simpy-warmup)
![](../attachments/screenshot-2024-02-27-at-230102.png)

## `SimPy` Hairdresser Example
In the next chunk we see the basic predefined parameters or assumptions of the model. We observe that a **seed**, the **number of hairdressers**, the **minimum** and **maximum times** for a haircut, the **expected arrival time** between customers, the **simulation time**, and the **total number of customers** we expect are specified.
Additionally, three global variables are initialized that we will use to collect simulation data: **wait time, service time, and the service completion minute**.

```python
SEED = 2023

WORKERS = 1

MIN_TIME_WITH_CUSTOMER = 15

MAX_TIME_WITH_CUSTOMER = 30

ARRIVALS_TIME = 10 # We expect a customer every 10 minutes

SIMULATION_TIME = 120

TOTAL_CUSTOMERS = 10

tw = 0.0 # Initialization of time waiting

st = 0.0 # Initialization of service time

end = 0.0 # Minute of finalization
```

In this initial function, we will define the **hair-cut event**. Given an initial time for the hair-cut, we will generate a random number to estimate the time of the hair-cut randomly for each client. Finally, we execute this event in the simulation in terms of time and record the data for further analysis.

```python
def haircut(customer):

global st # We access to the globally declared "st" variable

R = random.random() # Random number between 0 and 1

time = MAX_TIME_WITH_CUSTOMER - MIN_TIME_WITH_CUSTOMER

haircut_time = MIN_TIME_WITH_CUSTOMER + (time*R) # Uniform distribution for the haircut times

yield env.timeout(haircut_time) # We run this time in the simulation

print(" |=) Haircut ready for %s in %.2f minutes" % (customer,haircut_time))

st = st + haircut_time # We sum the time to the service time
```

The **customer** function will generate the customer's journey during the hair cutting process. We will record the time when the customer arrives, generate a queue, and start recording waiting times, in order to subsequently record the cutting time and simulate this process in terms of time in the global simulation.
Finally, we will record the completion time of the haircut for the customer.

```python
def customer (env, name, worker):

global tw

global end

arrival = env.now # store arrival time for client

print ("---> %s arrives at %.2f" % (name, arrival))

with workers.request() as request: # Wait for turn

yield request # Start Haircut

come_in = env.now # We store the starting minute

wait = come_in - arrival # Calculate waiting time

tw = tw + wait # Sum up waiting times

print ("**** %s starts haircut at %.2f with a waiting time of %.2f" % (name, come_in, wait))

yield env.process(haircut(name)) # Start Haircut process

leave = env.now # Stores ending minute

print ("<--- %s leaves the Hairdresser at %.2f" % (name, leave))

end = leave # Conserves globally the last minute of the simulation
```

The **main** function will generate pseudo-random times for each of the clients, and execute the previous functions for each one of them, registering all the data for subsequent analysis.

```python
def main(env, worker):

arrival = 0

i = 0

for i in range(TOTAL_CUSTOMERS): # for n customers

R = random.random()

arrival = random.expovariate(1/ARRIVALS_TIME) # Simulate arrivals from

#exponential given the previous random number

yield env.timeout(arrival) # simulation time between arrivals

i += 1

env.process(customer(env, 'Customer %d' % i, worker))
```

To begin the simulation, we must set an initial seed. Then, we can initialize the simulation environment and allocate the resources (in this case, only the workers). We generate the simulation process using the main function and execute the simulation environment. Additionally, we will use the variables saved at the beginning to calculate a series of indicators of interest for the simulation that will be displayed at the end of the output.

```python
print ("------------------- Welcome to the Hairdresser ------------------")

random.seed (SEED) # set the seed

env = simpy.Environment() # Start the enviroment

workers = simpy.Resource(env, WORKERS) # Create the resources (workers)

env.process(main(env, workers)) # Starts main programm

env.run() # Starts the simulation

  

print ("\n---------------------------------------------------------------------")

print ("\nIndicators obtained: ")

  

aql = tw / end

print ("\nAverage queue length: %.2f" % aql)

awt = tw / TOTAL_CUSTOMERS

print ("Average waiting time = %.2f" % awt)

hu = (st / end) / WORKERS

print ("Hairdresser usage = %.2f" % hu)

print ("\n---------------------------------------------------------------------")
```
![](../attachments/screenshot-2024-02-28-at-113824.png)
After concluding the simulation, we can utilize the data collected to optimize the system that we have designed.

In this instance, it appears that a single employee is insufficient to satisfy the established demand, resulting in a rather significant wait time to be attended to.
We could examine the potential outcomes of hiring another worker.

We can also execute the simulation for a specific time instead of a specific number of customers. We just need to change the line "env.run" to the following command:

```python
env.run(unti=SIMULATION_TIME)
```

Where SIMULATION_TIME is a variable declared at the beginning of the program. Also, we must adjust themain function. Instead of “for i in range(TOTAL_CUSTOMERS):”, we will use an infinite loop: `while True:`

```python
def main(env, worker):

arrival = 0

i = 0

while True: # for n customers

R = random.random()

arrival = random.expovariate(1/ARRIVALS_TIME)

yield env.timeout(arrival)

i += 1

env.process(customer(env, 'Customer %d' % i, worker))

  

print ("------------------- Welcome to the Hairdresser ------------------")

random.seed (SEED) # set the seed

env = simpy.Environment() # Start the enviroment

workers = simpy.Resource(env, WORKERS) # Create the resources (workers)

env.process(main(env, workers)) # Starts main programm

env.run(until = SIMULATION_TIME) # Starts the simulation

  

print ("\n---------------------------------------------------------------------")

print ("\nIndicators obtained: ")

  

aql = tw / end

print ("\nAverage queue length: %.2f" % aql)

awt = tw / TOTAL_CUSTOMERS

print ("Average waiting time = %.2f" % awt)

hu = (st / end) / WORKERS

print ("Hairdresser usage = %.2f" % hu)

print ("\n---------------------------------------------------------------------")
```
![](../attachments/screenshot-2024-02-28-at-114045.png)



## `SimPy`: Linear Process with more than one sequential activity

That was an example of a very simple DES model, but in mos DES models, we will have more than one activity in our system.
Let's first consider a simple linear example, where patients queue for one activity, and then queue for a second activity as follows:
![](../attachments/screenshot-2024-02-28-at-114553.png)
```python
import simpy
import random

# Arrival generator for hospital

def patient_generator_h(env, h_inter, mean_register, mean_triage, receptionist, nurse):

patient_id = 1

while True:

p = activity_generator_h(env,mean_register,mean_triage,receptionist,nurse,patient_id)

env.process(p)

t = random.expovariate(1/h_inter)

yield env.timeout(t)

patient_id += 1
```

```python
# Activity generator

def activity_generator_h(env, mean_register, mean_triage, receptionist, nurse, patient_id):

time_entered_queue_registration = env.now

  

with receptionist.request() as req:

yield req

  

time_left_queue_registration = env.now

time_in_queue_registration = time_left_queue_registration - time_entered_queue_registration

print (" \\(o-o)/ Patient %s queued for registration %.2f minutes" % (patient_id, time_in_queue_registration))

  

registration_time = random.expovariate(1/mean_register)

yield env.timeout(registration_time)

  

time_entered_queue_triage = env.now

  

with nurse.request() as req:

yield req

  

time_left_queue_triage = env.now

time_in_queue_triage = time_left_queue_triage - time_entered_queue_triage

print (" \\(o-o)/ Patient %s queued for triage %.2f minutes" % (patient_id, time_in_queue_triage))

  

triage_time = random.expovariate(1/mean_triage)

yield env.timeout(triage_time)
```

```python
random.seed(2023)

env = simpy.Environment()

receptionist = simpy.Resource(env, capacity = 1)

nurse = simpy.Resource(env, capacity = 1)

  

h_inter = 8

mean_register = 2

mean_triage = 5

  

env.process(patient_generator_h(env, h_inter, mean_register, mean_triage, receptionist, nurse))

env.run(until=120)
```
![](../attachments/screenshot-2024-02-28-at-114724.png)

## `SimPy`: Non-linear Process with more than one sequential activity
Often in real world systems, not everything is linear. Different things might happen depending on certain conditions. For example, after triage a patient might be referred to a Ambulatory Care to diagnose a treatment to the patient without being admitted to the hospital overnight.

![](../attachments/screenshot-2024-02-28-at-114844.png)

```python
import simpy
import random

# Arrival generator for hospital

def patient_generator_h(env, h_inter, mean_register, mean_triage, mean_ac_assessment, mean_h_assessment, receptionist, nurse, ac_doctor, h_doctor):

patient_id = 1

  

while True:

p = activity_generator_h(env, mean_register, mean_triage, mean_ac_assessment, mean_h_assessment, receptionist, nurse, ac_doctor, h_doctor, patient_id)

env.process(p)

t = random.expovariate(1/h_inter)

  

yield env.timeout(t)

patient_id += 1
```

```python
# Activity generator

def activity_generator_h(env, mean_register, mean_triage, mean_ac_assessment, mean_h_assessment, receptionist, nurse, ac_doctor, h_doctor, patient_id):

time_entered_queue_registration = env.now

  

with receptionist.request() as req:

yield req

  

time_left_queue_registration = env.now

time_in_queue_registration = time_left_queue_registration - time_entered_queue_registration

print (" \\(o-o)/ Patient %s queued for registration %.2f minutes" % (patient_id, time_in_queue_registration))

  

registration_time = random.expovariate(1/mean_register)

yield env.timeout(registration_time)

  

time_entered_queue_triage = env.now

  

with nurse.request() as req:

yield req

  

time_left_queue_triage = env.now

time_in_queue_triage = time_left_queue_triage - time_entered_queue_triage

print (" \\(o-o)/ Patient %s queued for triage %.2f minutes" % (patient_id, time_in_queue_triage))

  

triage_time = random.expovariate(1/mean_triage)

yield env.timeout(triage_time)

  

# We now start a branching path. Some patients will be sent to the Ambulatory,

# but others will remain in the Hospital. We are going to split them out using

# probabilitie, so let's randomly sample from a uniform distribution to decide

# whether this patient goes to the AC or not.

decide_ac_branch = random.uniform(0,1)

  

# Now we can just use a conditional statement to determine the next activity

# for this patient. Let's first indicate the AC condition

if decide_ac_branch < 0.2:

# Inside each conditional statement we will indicate the same elements in

# the simulation as before, now for the doctor resource (AC or H)

time_entered_queue_ac_assessment = env.now

with ac_doctor.request() as req:

yield req

  

time_left_queue_ac_assessment = env.now

time_in_queue_ac_assessment = time_left_queue_ac_assessment - time_entered_queue_ac_assessment

print (" \\(o-o)/ Patient %s queued for ambulatory assessment %.2f minutes" % (patient_id, time_in_queue_ac_assessment))

  

ac_assessment_time = random.expovariate(1/mean_ac_assessment)

yield env.timeout(ac_assessment_time)

  

else:

  

time_entered_queue_h_assessment = env.now

with h_doctor.request() as req:

yield req

  

time_left_queue_h_assessment = env.now

time_in_queue_h_assessment = time_left_queue_h_assessment - time_entered_queue_h_assessment

print (" \\(o-o)/ Patient %s queued for hospital assessment %.2f minutes" % (patient_id, time_in_queue_h_assessment))

  

h_assessment_time = random.expovariate(1/mean_h_assessment)

yield env.timeout(h_assessment_time)
```

```python
random.seed(2023)

env = simpy.Environment()

  

receptionist = simpy.Resource(env, capacity = 1)

nurse = simpy.Resource(env, capacity = 1)

h_doctor = simpy.Resource(env, capacity = 2)

ac_doctor = simpy.Resource(env, capacity = 1)

  

h_inter = 8

mean_register = 2

mean_triage = 5

mean_ac_assessment = 10

mean_h_assessment = 15

  

env.process(patient_generator_h(env, h_inter, mean_register, mean_triage,

mean_ac_assessment, mean_h_assessment,

receptionist, nurse, ac_doctor, h_doctor))

env.run(until=120)
```
![](../attachments/screenshot-2024-02-28-at-120644.png)

## `SimPy` Storing Results

Sometimes we want to **store the results** over the simulation run so we can, for example, calculate the average queuing time across patients.

One way we could do this would be to set up a list to store the results we are interested in, and then add each patient's results to the list.

If we want to do that using generators we will need the **global keyword**.

```python
import simpy

import random

# Arrivals generator function

def patient_generator(env, wl_inter, mean_consult, nurse):

patient_id = 1

# keep generating indefinitely

while True:

# Create instance of activity generator

wp = activity_generator(env,mean_consult,nurse,patient_id)

# run the activity generator for this patient

env.process(wp)

# Sample time until next patient

t = random.expovariate(1/wl_inter)

# Freeze until that time has passed

yield env.timeout(t)

patient_id += 1
```

```python
# Activity generator function. This activity generator function normally

# describes arrivals journey

def activity_generator(env, mean_consult, nurse, patient_id):

  

# Strictly speaking, varaibles referenced outside of a function, and which

# aren't passed in, don't exist in the eyes of the function.

# This means that if we were to refer to a variable that we haven't passed

# in, and we make any sort of change to it, it will set up a NEW variable

# with the same name INSIDE the function. Usually we don't want that.

  

# By using the global keyword, we declare that the queuing_times_nurse_list

# list that we are referring to here is the same one we have declared OUTSIDE

# the function and not a new one. So when we add something to it here, it adds

# it to the global list, not a brand new list with the same name in the local

# environment of the function.

global queuing_times_nurse_list

  

time_entered_queue = env.now

#print ("---> Patient %s arrives at %.2f" % (patient_id, time_entered_queue))

# request a nurse from the Resources

with nurse.request() as req:

# Freeze until the request can be met

yield req

# Calculate time patient was queuing

time_left_queue = env.now

#print (" <--- Patient %s left queue at %.2f" % (patient_id, time_left_queue))

time_in_queue = time_left_queue - time_entered_queue

#print (" \\(o-o)/ Patient %s was waiting for %.2f minutes" % (patient_id, time_left_queue))

  

## Append the calculated time in queue for this patient to our global list

queuing_times_nurse_list.append(time_in_queue)

  

# Sample time spent with nurse

consultation_time = random.expovariate(1/mean_consult)

# Freeze until that time has passed

yield env.timeout(consultation_time)
```

```python
random.seed(2023)

# Set up the simulation enviroment

env = simpy.Environment()

# Set up resources

nurse = simpy.Resource(env, capacity = 1)

# Set up parameters

wl_inter = 5

mean_consult = 6

# Create the empty list in the global environment

queuing_times_nurse_list = []

# Start the arrivals generator

env.process(patient_generator(env,wl_inter, mean_consult, nurse))

# Run the simulation

env.run(until=120)

# Results

print("the average time in the queue is of", np.array(queuing_times_nurse_list).mean(), "minutes")

#Returns the average time in the queue is of 21.319259562848288 minutes
```


## `SimPy`: Multiple Runs
In a stochastic model, it is important that we do not just run a model once if we are looking ro draw insights from our results. This is because every single run of the simulation will have very different random samples for all the stochastic elements (arrival times, activity times, etc.)

As we have learned in the last module, for any simulation experiment, it is essential to replicate the experiment a bunch of times in order to have different results that we can aggregate.

This way we can take summary statistics over the results from each run to get more representative results from the model.

In SimPy, to run a simulation multiple times, we put all of the setup in a for loop, with the range of the replications we want to create. This will reset and start a new simulation for every run, so if we want to store individual simulation run results we either need to:

- Have a global list outside of the loop that stores the results from each run, or
- write the results of each run to file.

```python
# Set up number of replicas of the simulation and a seed

n_runs = 100

random.seed(2023)

  

# Create a file to store the results of each run and write the header

with open("nurse_results.csv", "w") as f:

writer = csv.writer(f, delimiter = ",")

writer.writerow(["Run", "Mean_Queue"])

  

for run in range(n_runs):

# Set up the simulation enviroment

env = simpy.Environment()

# Set up resources

nurse = simpy.Resource(env, capacity = 1)

# Set up parameters

wl_inter = 8

t_inter = 10

mean_consult = 10

mean_test = 3

# Create the empty list in the global environment

queuing_times_nurse_list = []

# Start the arrivals generators, in this case we have two.

env.process(patient_generator_weight_loss(env,wl_inter, mean_consult, nurse))

env.process(patient_generator_test(env,t_inter, mean_test, nurse))

# Run the simulation

env.run(until=120)

# Results

mean_queue = mean(queuing_times_nurse_list)

# Set up list to write to file in this run

list_to_write = [run, mean_queue]

# Store the results of this run in the file

with open("nurse_results.csv", "a") as f:

writer = csv.writer(f, delimiter = ",")

writer.writerow(list_to_write)
```

```python
results_df = pd.read_csv("nurse_results.csv")

average_mean_runs = results_df["Mean_Queue"].mean()

print("The average waiting time along all the replicas of the experiment is of", average_mean_runs, "minutes")

#Returns The average waiting time along all the replicas of the experiment is of 30.610686732718513 minutes
```

```python
import matplotlib.pyplot as plt

results_df.boxplot("Mean_Queue")

plt.show()
```
![](../attachments/screenshot-2024-02-28-at-122106.png)


