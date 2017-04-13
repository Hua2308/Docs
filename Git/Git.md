1. Revert local change and reset current branch with remote:
    * `$git reset --hard origin/\<local_branch\>`

2. Incoporate master branch changes with your working branch:
    * Merge
      *  `$git checkout <your_branch>` then `$git merge master` or,
      *  `$git merge master <your_branch>`
      *  Pros: Preserve intact commit history
      *  Cons: History is figure-cross merged, and may 'pollute' your local branch history.
    * Rebase
      *  Before rebase, make sure local changes have been pushed and is sync with master.
      *  `$git checkout <your_branch>` then `$git rebase -i origin/master` then `$git push origin master --force` or,
      *  `$git rebase -i origin/master <your_branch>` then `$git push origin master --force`
      *  Pros: Lineal history (B/c your commit always starts from the tail, so no figure-cross), and you can squash commits along the way.
      *  Cons: Rewrite your local branch history (b/c inject master history first)
    * For a visual comparison in flow diagram, see [Merge vs Rebase](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)

3. Clean up commit history(i.e. Squash commits):
      * When rebase local branch with remote:
         *  `$git rebase -i master` then edit 'pick' to 'squash' for each commit to be squashed.
         *  ~~Then force flush local commit history: `$git push origin <branch>` --force~~
      * Just local clean up, no actual branch rebase:
         *  `$git rebase -i HEAD~<number_of_commits>`



