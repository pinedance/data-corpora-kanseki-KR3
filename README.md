# corpora-kanseki-한적자부

[ksnseki_repository](http://www.kanripo.org/)에 있는 자부(子部) 의가류(醫家類) 데이터

* [漢リポ Kanseki Repository](http://www.kanripo.org/)
* [漢リポ Kanseki Repository Github repo](https://github.com/kanripo)

## 방법

create `Kanseki_Repository.gitmodules` file

```bash
poetry run python build_gitmodules.py
```

clone submodules

```bash
bash git_clone_Kanseki_Repository.sh
```

## check

```bash
git submodule status
```

## update

```bash
git submodule
git submodule update --remote
```

## Remove Submodule

REF: [How do I revert my changes to a git submodule?](https://stackoverflow.com/a/27415757)

```bash
git submodule
git submodule deinit <path_to_submodule>
git rm <path_to_submodule>
rm -rf .git/modules/<path_to_submodule>
git commit -m "Removed submodule <path_to_submodule>"
```

remove all

```bash
git submodule
git submodule foreach git submodule deinit
git submodule foreach git rm
rm -rf .git/modules
git commit -m "Removed all submodules"
```


## RESET Submodules

REF: [How do I revert my changes to a git submodule?](https://stackoverflow.com/a/27415757)

```bash
git submodule
git submodule deinit -f .
git submodule update --init
```

REF: https://unstop.com/blog/git-submodule

## Download Data from git repo

```bash
curl -L -o corpora.txt "https://github.com/pinedance/data-corpora-kanseki-KR3/raw/main/DIST/KR3e_merged.txt"
```

