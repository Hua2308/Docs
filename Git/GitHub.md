Best practice:

1. Branch 
    * One story one branch. Keep the story small and conhensive so that it is easier for code review.
    * Be cautious to merge any non-master branch. One reason is that it will bring in all non-squash'ed commit history.

2. Pull request 
    * Before creating PR, make sure local branch has merged to master, and resolve all conflicts.
    * Before merging PR, make sure squash all commits(through command line) including the one for PR (through GitHub UI)
    * After merging PR, delete the branch
    
