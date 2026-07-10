# Contributing to NK AI

First off, thank you for considering contributing to NK AI! It's people like you that make the open-source community such a great place to learn, inspire, and create.

## Branch Naming Convention

We use a standardized branch naming convention to keep our repository organized. Please name your branches using the following format:

`[type]/[issue-number]-[short-description]`

**Types:**
- `feat/`: For new features (e.g., `feat/12-add-search-bar`)
- `fix/`: For bug fixes (e.g., `fix/34-resolve-login-crash`)
- `docs/`: For documentation changes
- `chore/`: For maintenance tasks, dependency updates, etc.
- `refactor/`: For code refactoring without adding features or fixing bugs

## Commit Convention

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification for our commit messages. This helps us generate changelogs automatically and keeps our history readable.

Format:
`<type>[optional scope]: <description>`

**Examples:**
- `feat(auth): add google sign-in support`
- `fix(search): resolve null pointer exception on empty query`
- `docs(readme): update getting started instructions`
- `chore(deps): bump react from 18.2.0 to 18.3.0`

## Pull Request (PR) Process

1. **Ensure your code is up to date:** Rebase or merge from the main branch before submitting your PR.
2. **Use the PR Template:** Fill out the provided Pull Request template completely.
3. **Tests:** Ensure that all existing tests pass and write new tests for your feature or bug fix.
4. **Self-Review:** Perform a self-review of your code before requesting a review.
5. **Request Review:** Assign at least one core contributor to review your PR.
6. **Address Feedback:** Be responsive to feedback and make the necessary changes. Once approved, a maintainer will merge your PR.

## Coding Standards

To maintain a high-quality codebase, please adhere to the following standards:
- **EditorConfig:** We use an `.editorconfig` file. Ensure your editor is configured to use it.
- **Linting & Formatting:** Ensure your code passes all linters and formatters before committing.
- **Python (Django):** Follow PEP 8 guidelines. Keep views thin and logic in services/models where appropriate.
- **JavaScript/TypeScript (React):** Use functional components and hooks. Follow standard ESLint/Prettier rules.
- **Documentation:** Comment complex logic and keep README files up to date if you add new environment variables or change architecture.
