# My Python project

## TODO

- [ ] Update your LICENSE text, or set the LICENSE that fit your repository.
- [ ] Update the main title of this document to fit your repository, and add
      a description according to the purpose of the project.
- [ ] Update the name of your module and references to it.
- [ ] Update all the TODO placeholders in the repository at your convenience.
- [ ] Remove this TODO section.

## Getting started

### Once tasks

- (when not using toolbox-sh) Install [poetry](#):
  `sudo dnf install -y python3-poetry`
- Install [direnv](#): `sudo dnf install -y direnv`
- Install `toolbox`: `sudo dnf install -y toolbox`
- Install `toolbox.sh`: `git clone https://github.com/little-engineer-2025/toolbox-sh.git; cd toolbox.sh; ./toolbox.sh install`
- Prepare `.envrc`: `cat > .envrc <<< 'export TOOLBOX="dev"'`
- Allow `.envrc`: `direnv allow`
- Create the toolbox: `toolbox.sh create`
- Enter toolbox: `toolbox.sh enter`

### Frequent tasks

- Install dependencies: `make deps`
- Code at `hello_world`
- Unit test at `test`
- Apply format, run linter, and run unit tests by: `make all`
- Get help by: `make help`

**If you are using [toolbox.sh](https://github.com/little-engineer-2025/toolbox-sh)**

- Create file `.envrc` with something like:

```raw
# TODO Update the name for your toolbox
export TOOLBOX="my-project-dev"
```

- Create symlink to `.envrc`: `ln -svf .envrc .env`
- Allow file for direnv: `direnv allow`

> .env and .envrc files are ignored (repo and container).

### Contributing

See: [Contributing Guidelines](docs/CONTRIBUTING.md).

### Security Issues

See: [Security Issues](docs/SECURITY.md).


### Architecture Decision Records

See: [ADR](docs/adr/).

## References

- [poetry](https://python-poetry.org/).
- [direnv](https://direnv.net/).
- [flask](https://flask.palletsprojects.com/en/stable/).

