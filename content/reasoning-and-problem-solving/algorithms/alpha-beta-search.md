---
title: Alpha-Beta Search
---

```
function ALPHA-BETA-SEARCH(game, state) returns an action
	player ←game.TO-MOVE(state)
	value, move ← MAX-VALUE(game, state,−∞,+∞)
	return move
```

```
function MAX-VALUE(game, state,α, β) returns a (utility, move) pair
	if game.IS-TERMINAL(state) then return game.UTILITY(state, player ), null
	v ← −∞
	for each action in game.ACTIONS(state) do
		v2 , a2 ← MIN-VALUE(game, game.RESULT(state, action),α, β)
		if v2 > v then
			v, move ←v2 , action
			α ← MAX(α, v)
		if v ≥ β then return v, move
	return v, move
```
 
 ```
 function MIN-VALUE(game, state,α, β) returns a (utility, move) pair
	if game.IS-TERMINAL(state) then return game.UTILITY(state, player ), null
	v ← +∞
	for each action in game.ACTIONS(state) do
		v2 , a2 ← MAX-VALUE(game, game.RESULT(state, action),α, β)
		if v2 < v then
			v, move ←v2 , action
			β ← MIN(β, v)
		if v ≤ α then return v, move
	return v, move
 ```