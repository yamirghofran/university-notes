---
title: Heuristic Alpha-Beta Tree Search
---

A heuristic evaluation (EVAL function) function allows us to treat non-terminal nodes as if they were terminal.

We introduce a `IS-CUTOFF` function instead of `IS-TERMINAL` that returns True for terminal states, but also for other states.

H-MINIMAX(s,d) = 
- EVAL(s, MAX) if IS-CUTOFF(s, d)
- $\text{max}_\text{a in Actions(s)}$ H-MINIMAX(RESULT(s,a), d+1) if TO-MOVE(s) = MAX
- $\text{min}_\text{a in Actions(s)}$ H-MINIMAX(RESULT(s,a), d+1) if TO-MOVE(s) = MIN

## Eval Functions
EVAL(s,p) returns:
- UTILITY(s, p) for terminal states
- UTILITY(loss, p) ⇐ EVAL(s,p) ⇐ UTILITY(win, p) for non-terminal states

EVAL function should:
- not take too long
- be strongly correlated with chances of winning

In general, eval functions will take into account **features** of the state
- e.g. in chess it might be the number and types of pieces each player still has on the board
- functions that calculate based on the weight of each feature are called "weighted linear functions"
Ideally, it should represent the expected value:
- if 80% of the states lead to 1, and 20% lead to 0, then it should return 0.8
## Cutting off search
The basic implementation just replaces IS-TERMINAL with IS-CUTOFF and UTILITY with EVAL
- Quiescence search only returns True for IS-CUTOFF for positions that don't have a big risk (e.g that the opposite player could capture the queen next)
- Singular extensions allow for prioritizing moves that are clearly better, over moves that just push the horizon (i.e. moves that have little consequence but keep going beyond the depth we calculate)

## Forward Pruning
Removing moves that appear bad (even if they might actually be good)
- saves computation, but might lead to suboptimal outcomes
- a kind of Type B strategy
[Beam Search](/reasoning-and-problem-solving/algorithms/beam-search) considers only the best n moves (according to EVAL)
- there are learning versions of this, using probabilities of past games
- with a good enough EVAL, it can still beat other systems using less time
Late move reduction: assumes "good move ordering", and reduces the depth explored for them

Applying all these techniques we can get to around 8 ply on a regular computer, 14 ply on a powerful one (enough to beat most humans)

30 ply, doable by systems like STOCKFISH that also use extensive databases of past games, is enough to beat virtually any human.

## Other Methods
For chess, and other games, we don't always need search:
- Table lookups of opening moves (usually based on human expertise and books) is the most common strategy
- Table lookups of end-games (usually based on computer generated end-game strategies) is usually applied