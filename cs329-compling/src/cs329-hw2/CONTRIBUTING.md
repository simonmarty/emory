# cs329-hw2

## Cloning this repo

Copy this in a shell

```
git clone https://www.github.com/simonmarty/cs329-hw2.git
```

## Starting work on a new feature

All `<>` symbols shouldn't actually be included when you write these commands :)

```
git checkout -b <new-feature> # -b creates the branch if it doesn't exist
git push origin <new-feature>
```
Now you can do some work then
```
git add .
git commit -m "<explain what you did here>"
git push
```
When you're done with your feature and have done the above, open a pull request from
`<new-feature>` to `master` and merge. Delete the remote branch.
Delete the old branch
```
git checkout master
git branch -d <new-feature> # -d stands for delete
```
Have fun!
