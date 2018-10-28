# Reliable Transport

original [readme file](README)

For **Reliable** transport
By **Flow control**
- stop and wait
- go back n
- selective repeat

## Reliable condition
Your sender should provide reliable service under the following network conditions:
- Loss: arbitrary levels; you should be able to handle periods of 100% packet loss.
- Corruption: arbitrary types and frequency.
- Re-ordering: may arrive in any order, and
- Duplication: you could see a packet any number of times.
- Delay: packets may be delayed indefinitely (but in practice, generally not more than
10s).

### edge cases
- TODO related #2 issue


