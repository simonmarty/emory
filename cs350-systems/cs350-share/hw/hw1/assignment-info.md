# Information for Assignment 1 and related Notes

## Coordinates of a given prime

Structure: `(pt, index, bit)` 

| var | value|
|------|-------|
| pt | `pointer` |
| index | `0-255` |
| bit | `0-31` |

### Incrementing

Remember to carry. <br>
i.e.if we try to increment `bit = 31` <br>
`bit = 0` and increment `index` <br>
If `index` is `255` , `index = 0` and `pt = pt -> next` 

