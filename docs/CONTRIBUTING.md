# How to contribute?

- Check if the change already exist in some issue
  [here](https://github.com/little-engineer-2025/template-python3/issues).
  <!-- TODO update the reference to your repository -->
- If it does not exist, open a new issue using the template that fit better the
  change.
- Fork the repository [here](https://github.com/little-engineer-2025/template-python3/fork)
  into your SCM account.
  <!-- TODO update the reference to your repository -->
- Clone your forked repository into your workspace.
- Create a branch: `git checkout -b my_awesome_feature`
- Code your change and unit test.
- Run local checks: `make all`
- Do commits frequently.
- When happy with the changes, push your change and open a PR.
- Ping some owner to review the changes if not attended in 7 days.
- If any change suggested, or clarification on the changes, comment and update
  changes, and ping the reviewer to do another round.
- PR merged! Thanks for your collaboration :)

Happy coding! :)

## Developing Guidelines

<!--
TODO Create the `docs/adr/...` files as needed depending on your needs.
     See the adr-tools below.
-->

- Check the ADRs at: [todo](#).
- Use [adr-tools](https://github.com/npryce/adr-tools) for managing records.
  It is installed inside the toolbox when it is created the first time.

Some references:

- [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
- [Managing Architecture Decision Records with ADR-Tools](https://www.hascode.com/managing-architecture-decision-records-with-adr-tools/).
- [Architectural Decision Records](https://adr.github.io/).

## Commit formats

- The repository try to follow [conventional commits](https://www.conventionalcommits.org/).

```raw
type: title

Explain the reason of the changes if not trivial.

close: #issue

[Co-Authored-By: First Last name <email@example.org>]
Signed-By: First Last name <email@example.org>
```
- Please reference the issue 
- For recognition of other collaborators, please consider to add
  `Co-Authored-By: ...` to reference them.
- Please sign all your commits.

## PR format

```raw
Summary of the changes

TODO

- [ ] The pipeline pass.
- [ ] All the commits follow the format above (automate in future).
- [ ] Every commit in the PR pass at least the unit tests locally (better
      integration tests also).
- [ ] All the doubts about the change are resolved, even trivial ones.
- [ ] All the required changes are addressed, and commit reorg if needed.

close: #issue
```

