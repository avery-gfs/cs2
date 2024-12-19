Let's define a *paren expression* as a string made up of only `(` and `)` characters. We'll call a paren expression *balanced* if the parentheses can be matched such that:

1) Each `(` character matches some `)` character that comes after it.

2) Each `)` character matches some `(` character that comes before
it.

3) Each parenthesis is matched with exactly one other parenthesis.

4) The characters between each set of matching parentheses also form a balanced parenthesis expression.

The following paren expressions *are* balanced:

- `""`
- `"()"`
- `"()()"`
- `"(())"`
- `"(()())"`
- `"()(()())()"`

The following paren expressions *are not* balanced:

- `"("`
- `")("`
- `"(()"`
- `"())(()"`

The following properties are necessary (but not sufficient) for a paren expression to be balanced:

1) The expression must not start with `)` or end with `(`.

2) The expression must contain an even number of characters.

3) The expression must contain an equal number of `(` and `)` characters.

Write code that determines whether a given paren expression is balanced.
