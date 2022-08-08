`git reset --keep HEAD@{1}`

## how to undo after pull

- get list activity with command `git reflog`
- you will see 
    ```
    6b5726 (HEAD -> master, origin/master, origin/HEAD) HEAD@{0}: pull: Fast-forward
    ec03cf6 HEAD@{1}: checkout: moving from feature/rekap-klasifikasi to master
    ```
- select id for undo, eg : `git reset --soft ec03cf6`
- and every change will be staged
- end