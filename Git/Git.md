1. Update local branch after 'Git pull' remote changes:
    * Method a. $git reset --hard origin/\<local_branch\>
    * Method b. $git rebase \<remote_branch_to_be_as_base\> \<local_branch\>

2. Squash commits:
    * $git rebase -i HEAD~\<number_of_commits\>, then edit 'pick' to 'squash' for each commit to be squashed (Reference: https://ariejan.net/2011/07/05/git-squash-your-latests-commits-into-one/)
    
