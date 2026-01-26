# Testing

> [!NOTE]
> Return back to the [README.md](README.md) file.

This document outlines the testing strategy and evidence for **StudyStack**, a Django-based full stack web application built as part of the Code Institute Milestone 3 (Back End Development) project.

Testing has been carried out throughout development using a combination of **automated tests**, **manual user acceptance testing**, and **external validation tools**, in line with the assessment requirements.

---

## Code Validation

### HTML

> [!NOTE]
> HTML validation was carried out using a [**custom Python CLI tool**](https://github.com/yenmangu/w3c-command-line-validator) that consumes the **W3C Nu HTML Checker HTTP API**.
>
> Validation was performed **against deployed URLs**, ensuring that the results reflect the fully rendered production state of the application rather than local templates.
>
> The tool was run against all major routes in the application, including authenticated pages and querystring-based routes.
>
> **Full validation output is provided as evidence** in the following report:
>
> [Validation Report](documentation/validation/w3c-validation-report-20_01_26.txt)

| Page / Template      | URL (Deployed)                                                                                                                                                                     | Result | Evidence   |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ---------- |
| Home / Resource List | [https://study-stack-63fdd524a632.herokuapp.com/](https://study-stack-63fdd524a632.herokuapp.com/)                                                                                 | Pass   | See report |
| Resource Detail      | [https://study-stack-63fdd524a632.herokuapp.com/resources/python-tutorial-official/](https://study-stack-63fdd524a632.herokuapp.com/resources/python-tutorial-official/)           | Pass   | See report |
| Resource Create      | [https://study-stack-63fdd524a632.herokuapp.com/create/](https://study-stack-63fdd524a632.herokuapp.com/create/)                                                                   | Pass   | See report |
| Resource Update      | [https://study-stack-63fdd524a632.herokuapp.com/resources/python-tutorial-official/edit/](https://study-stack-63fdd524a632.herokuapp.com/resources/python-tutorial-official/edit/) | Pass   | See report |
| Resource Delete      | POST-only (CSRF-protected form action)                                                                                                                                             | Pass   | See report |
| Authentication Pages | [https://study-stack-63fdd524a632.herokuapp.com/accounts/login/](https://study-stack-63fdd524a632.herokuapp.com/accounts/login/)                                                   | Pass   | See report |

No HTML errors were reported for any validated routes.
Any informational messages returned by the validator did not affect functionality, accessibility, or document validity.

---

### CSS

All custom CSS files were validated using the **W3C Jigsaw CSS Validator**.

> [!NOTE]
> The W3C Jigsaw CSS Validator reports warnings when validating CSS Custom Properties that reference other custom properties using `var()`.
>
> In this project, a layered design-token approach is used in `theme.css`, where semantic colour variables (e.g. `--ss-academic-blue`) are derived from base variables. While this is fully valid and supported by all modern browsers, the validator’s static analysis cannot resolve nested `var()` references and therefore reports false-positive colour errors.
>
> These messages do not indicate invalid CSS and do not affect rendering, accessibility, or browser compatibility.
>
> CSS custom properties are a core feature of modern CSS and are used extensively by frameworks such as Bootstrap 5.

| File      | Purpose                   | Result                  | Screenshot                                                         |
| --------- | ------------------------- | ----------------------- | ------------------------------------------------------------------ |
| style.css | Custom site styles        | Pass                    | ![screenshot](./documentation/validation/style-css-validation.png) |
| theme.css | Component-specific styles | Errors - see note above | ![screenshot](./documentation/validation/theme-css-validation.png) |

Any warnings encountered were related to modern CSS features and did not impact browser support or accessibility.

---

### Python

Python code quality was assessed through:

- Django’s built-in system checks
- Manual review against **PEP8** standards
- Automated Django test execution

All custom Python files follow consistent naming, indentation, and descriptive variable conventions.

---

## Automated Testing

Automated tests were written using **Django’s built-in test framework** (`django.test.TestCase`). These tests focus on core application logic, access control, and data integrity.

### Model Tests

| Test            | Purpose                                         | Result |
| --------------- | ----------------------------------------------- | ------ |
| Slug uniqueness | Ensure unique slugs are generated automatically | Pass   |
| Status defaults | Confirm default status is set correctly         | Pass   |
| Relationships   | Validate Resource–Subject relationships         | Pass   |

### View Tests

| Test                       | Purpose                               | Result |
| -------------------------- | ------------------------------------- | ------ |
| Resource list visibility   | Published vs draft visibility rules   | Pass   |
| Resource detail access     | Author / non-author access control    | Pass   |
| Create resource            | Logged-in users can create resources  | Pass   |
| Update resource            | Only authors can edit their resources | Pass   |
| Delete resource (positive) | Author can delete resource            | Pass   |
| Delete resource (negative) | Non-author receives 403               | Pass   |

### Form Tests

| Test                    | Purpose                                               | Result |
| ----------------------- | ----------------------------------------------------- | ------ |
| ResourceForm valid data | Form saves correctly                                  | Pass   |
| Multiple new subjects   | Comma-separated subjects are created and deduplicated | Pass   |
| Invalid submission      | Form errors displayed correctly                       | Pass   |

All automated tests pass successfully and are run before deployment.

---

## Responsiveness

The application was tested across multiple viewport sizes using browser developer tools and real devices.

| Page                  | Mobile | Tablet | Desktop | Notes                    |
| --------------------- | ------ | ------ | ------- | ------------------------ |
| Home / Resource List  | Pass   | Pass   | Pass    | Grid adapts cleanly      |
| Resource Detail       | Pass   | Pass   | Pass    | Content stacks correctly |
| Create / Update Forms | Pass   | Pass   | Pass    | Inputs remain usable     |
| Authentication        | Pass   | Pass   | Pass    | No overflow issues       |

### Responsiveness Evidence

| Page                           | Mobile                                                                                | Tablet                                                                                | Desktop                                                                                |
| ------------------------------ | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Home / List                    | ![View Screenshot](./documentation/responsiveness/sizes/home-mobile.png)              | ![View Screenshot](./documentation/responsiveness/sizes/home-tablet.png)              | ![View Screenshot](./documentation/responsiveness/sizes/home-desktop.png)              |
| Detail                         | ![View Screenshot](./documentation/responsiveness/sizes/detail-mobile.png)            | ![View Screenshot](./documentation/responsiveness/sizes/detail-tablet.png)            | ![View Screenshot](./documentation/responsiveness/sizes/detail-desktop.png)            |
| Subjects                       | ![View Screenshot](./documentation/responsiveness/sizes/subjects-mobile.png)          | ![View Screenshot](./documentation/responsiveness/sizes/subjects-tablet.png)          | ![View Screenshot](./documentation/responsiveness/sizes/subjects-desktop.png)          |
| Subject-Resources (Join table) | ![View Screenshot](./documentation/responsiveness/sizes/subject-resources-mobile.png) | ![View Screenshot](./documentation/responsiveness/sizes/subject-resources-tablet.png) | ![View Screenshot](./documentation/responsiveness/sizes/subject-resources-desktop.png) |
| Add/Edit Resource Form         | ![View Screenshot](./documentation/responsiveness/sizes/add-edit-resource-mobile.png) | ![View Screenshot](./documentation/responsiveness/sizes/add-edit-resource-tablet.png) | ![View Screenshot](./documentation/responsiveness/sizes/add-edit-resource-desktop.png) |
| Comment Form                   | ![View Screenshot](./documentation/responsiveness/sizes/comment-form-mobile.png)      | ![View Screenshot](./documentation/responsiveness/sizes/comment-form-tablet.png)      | ![View Screenshot](./documentation/responsiveness/sizes/comment-form-desktop.png)      |
| Auth (login)                   | ![View Screenshot](./documentation/responsiveness/sizes/auth-login-mobile.png)        | ![View Screenshot](./documentation/responsiveness/sizes/auth-login-tablet.png)        | ![View Screenshot](./documentation/responsiveness/sizes/auth-login-desktop.png)        |

---

## Browser Compatibility

The deployed application was tested on the following browsers:

| Browser      | Result | Notes                   |
| ------------ | ------ | ----------------------- |
| Chrome       | Pass   | Full functionality      |
| Opera        | Pass   | No compatibility issues |
| Safari       | Pass   | Tested on macOS         |
| iOS (Safari) | Pass   | Tested on iPhone 11 Pro |

### Browser Compatibility Breakdown

Each core feature was manually tested across multiple browsers and devices to ensure consistent behaviour and layout.

| Feature                        | Chrome                                                                           | Opera                                                                   | Safari                                                                   | iOS (Safari)                                                          |
| ------------------------------ | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| Home (list)                    | ![View Screenshot](./documentation/browser/chrome/home-desktop.png)              | ![View Screenshot](./documentation/browser/opera/home.png)              | ![View Screenshot](./documentation/browser/safari/home.png)              | ![View Screenshot](./documentation/browser/iOS/home.png)              |
| Detail                         | ![View Screenshot](./documentation/browser/chrome/detail-desktop.png)            | ![View Screenshot](./documentation/browser/opera/detail.png)            | ![View Screenshot](./documentation/browser/safari/detail.png)            | ![View Screenshot](./documentation/browser/iOS/detail.png)            |
| Subjects                       | ![View Screenshot](./documentation/browser/chrome/subjects-desktop.png)          | ![View Screenshot](./documentation/browser/opera/subjects.png)          | ![View Screenshot](./documentation/browser/safari/subjects.png)          | ![View Screenshot](./documentation/browser/iOS/subjects.png)          |
| Subject-Resources (Join table) | ![View Screenshot](./documentation/browser/chrome/subject-resources-desktop.png) | ![View Screenshot](./documentation/browser/opera/subject-resources.png) | ![View Screenshot](./documentation/browser/safari/subject-resources.png) | ![View Screenshot](./documentation/browser/iOS/subject-resources.png) |
| Add/Edit Resource              | ![View Screenshot](./documentation/browser/chrome/add-edit-resource-desktop.png) | ![View Screenshot](./documentation/browser/opera/add-edit-resource.png) | ![View Screenshot](./documentation/browser/safari/add-edit-resource.png) | ![View Screenshot](./documentation/browser/iOS/add-edit-resource.png) |
| Add/Edit Comment               | ![View Screenshot](./documentation/browser/chrome/comment-edit-desktop.png)      | ![View Screenshot](./documentation/browser/opera/add-edit-comment.png)  | ![View Screenshot](./documentation/browser/safari/add-edit-comment.png)  | ![View Screenshot](./documentation/browser/iOS/add-edit-comment.png)  |
| Auth (login)                   | ![View Screenshot](./documentation/browser/chrome/auth-login-desktop.png)        | ![View Screenshot](./documentation/browser/opera/auth-sign-in.png)      | ![View Screenshot](./documentation/browser/safari/auth-sign-in.png)      | ![View Screenshot](./documentation/browser/iOS/auth-login.png)        |
| Auth (logout)                  | ![View Screenshot](./documentation/browser/chrome/auth-logout.png)               | ![View Screenshot](./documentation/browser/opera/auth-logout.png)       | ![View Screenshot](./documentation/browser/safari/auth-logout.png)       | ![View Screenshot](./documentation/browser/iOS/auth-logout.png)       |
| Auth (registration)            | ![View Screenshot](./documentation/browser/chrome/auth-registration.png)         | ![View Screenshot](./documentation/browser/opera/auth-registration.png) | ![View Screenshot](./documentation/browser/safari/auth-registration.png) | ![View Screenshot](./documentation/browser/iOS/auth-registration.png) |

#### Notes

- All browsers tested fully support:
  - semantic HTML5 elements
  - modern CSS (Flexbox, Grid, CSS filters, custom properties)
  - JavaScript ES modules used in the project
- No polyfills or browser-specific fallbacks were required.
- Internet Explorer is not supported, as it is deprecated and not required by the assessment brief.

Browser testing was carried out using a combination of real devices and browser developer tools.

---

## Lighthouse Audit

Lighthouse audits were conducted using Chrome DevTools on key user-facing pages to assess performance, accessibility, best practices, and SEO. Tests were run in both **mobile** and **desktop** modes using Lighthouse’s default throttling profiles.

Screenshots of the audit results are stored in `documentation/lighthouse/reports/`.

### Lighthouse Results Table

| Page / View                     | Mobile Result | Desktop Result | Desktop Screenshot                                                                   | Mobile Screenshot                                                                   |
| ------------------------------- | ------------- | -------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| Home                            | Good          | Excellent      | [View screenshot](documentation/lighthouse/reports/home-desktop.png)                 | [View screenshot](documentation/lighthouse/reports/home-mobile.png)                 |
| Browse by Subject               | Good          | Excellent      | [View screenshot](documentation/lighthouse/reports/browse-subjects-desktop.png)      | [View screenshot](documentation/lighthouse/reports/browse-subjects-mobile.png)      |
| Resource Detail                 | Good          | Excellent      | [View screenshot](documentation/lighthouse/reports/detail-desktop.png)               | [View screenshot](documentation/lighthouse/reports/detail-mobile.png)               |
| Resource Detail (No Comments)   | Good          | Excellent      | [View screenshot](documentation/lighthouse/reports/detail-no-comments-desktop.png)   | [View screenshot](documentation/lighthouse/reports/detail-no-comments-mobile.png)   |
| Resource Detail (With Comments) | Good          | Excellent      | [View screenshot](documentation/lighthouse/reports/detail-with-comments-desktop.png) | [View screenshot](documentation/lighthouse/reports/detail-with-comments-mobile.png) |
| Filtered Results                | Good          | Excellent      | [View screenshot](documentation/lighthouse/reports/filter-results-desktop.png)       | [View screenshot](documentation/lighthouse/reports/filter-results-mobile.png)       |
| Create Resource                 | Excellent     | Excellent      | [View screenshot](documentation/lighthouse/reports/create-desktop.png)               | [View screenshot](documentation/lighthouse/reports/create-mobile.png)               |
| Sign In                         | Excellent     | Excellent      | [View screenshot](documentation/lighthouse/reports/sign-in-desktop.png)              | [View screenshot](documentation/lighthouse/reports/sign-in-mobile.png)              |
| Sign Up                         | Excellent     | Excellent      | [View screenshot](documentation/lighthouse/reports/signup-desktop.png)               | [View screenshot](documentation/lighthouse/reports/signup-mobile.png)               |
| Logout                          | Excellent     | Excellent      | [View screenshot](documentation/lighthouse/reports/logout-desktop.png)               | [View screenshot](documentation/lighthouse/reports/logout-mobile.png)               |

### Notes on Results

Desktop Lighthouse audits consistently achieved Excellent scores across all categories due to higher available bandwidth and the absence of simulated network throttling. Mobile audits achieved **Good** results, with minor reductions primarily caused by Lighthouse’s slow network simulation, initial image loading costs, and the presence of render-blocking CSS required for layout stability.

Some stylesheets (Bootstrap and theme-level CSS variables) are intentionally render-blocking to ensure visual consistency and prevent layout shift during initial paint. During optimisation, deferring theme-level CSS resulted in increased layout shift and reduced Lighthouse scores. The final implementation therefore reflects a deliberate trade-off favouring visual stability (CLS within “Good” thresholds) over aggressive CSS deferral

These differences are expected and acceptable for real-world mobile usage.

### Image Optimisation & CLS Fix

Initial Lighthouse audits identified a significant layout shift caused by an
oversized default placeholder image (over 4500px wide) being rendered at card
dimensions (~640px).

This was resolved by:

- resizing the default placeholder image to an appropriate maximum size,
- generating modern formats (AVIF / WebP),
- ensuring explicit width and height attributes were applied.

After optimisation:

- **CLS was reduced to 0.048**, within the “Good” Core Web Vitals threshold.

  > [!NOTE]
  > This value falls well within Google’s “Good” Core Web Vitals threshold (CLS ≤ 0.1).

- **LCP improved to ~2.0s** on mobile.
- No layout shift culprits were reported for the main content container.

### Performance Optimisations Applied

- Deferred non-critical custom stylesheets using the `media="print"` and `onload` technique.
- Optimised resource card images via Cloudinary automatic format and quality selection.
- Enabled lazy-loading for below-the-fold images.
- Loaded JavaScript files using the `defer` attribute to avoid blocking the critical rendering path.

Bootstrap CSS was intentionally kept render-blocking to preserve layout integrity during initial page render.

These decisions reflect an understanding of real-world performance trade-offs, prioritising layout stability and user experience over artificially maximised audit scores.

---

## Defensive Programming

Manual testing was carried out to ensure the application behaves safely and predictably under invalid or unexpected user actions.
All defensive behaviours are enforced server-side and verified via manual interaction.

| Feature                           | Expectation              | Result | Notes                                      | Evidence                                                                 |
| --------------------------------- | ------------------------ | ------ | ------------------------------------------ | ------------------------------------------------------------------------ |
| Unauthorised edit (Not logged in) | Anonymous users blocked  | Pass   | Redirected to login before edit allowed    | ![Screenshot](./documentation/defensive/unauth_edit_redirect.gif)        |
| Unauthorised edit (Non-author)    | Non-authors blocked      | Pass   | Custom 403 Forbidden page returned         | ![Screenshot](./documentation/defensive/test-403.png)                    |
| Unauthorised delete               | Non-authors blocked      | Pass   | Resource retained; delete action denied    | ![Screenshot](./documentation/defensive/forced-delete-forbidden.png)     |
| Invalid form input                | Validation errors shown  | Pass   | Server-side validation prevents submission | ![Screenshot](./documentation/defensive/server-side-form-validation.png) |
| Missing resource                  | Graceful failure         | Pass   | Custom 404 page displayed                  | ![Screenshot](./documentation/defensive/test-404.png)                    |
| Internal server error             | Application fails safely | Pass   | Custom 500 page rendered                   | ![Screenshot](./documentation/defensive/test-500.png)                    |
| Password too common               | Weak passwords rejected  | Pass   | Django password validators enforced        | ![Screenshot](./documentation/defensive/password-too-common.png)         |
| Password too short                | Minimum length enforced  | Pass   | Browser-independent validation confirmed   | ![Screenshot](./documentation/defensive/password-too-short.png)          |
| Comment form (Not authenticated)  | Anonymous users blocked  | Pass   | Comment form hidden / access denied        | ![Screenshot](./documentation/defensive/comment-form-not-auth.png)       |

---

## Implemented User Story Testing

User stories were manually verified against acceptance criteria.
All user stories shown in the project board were marked as _Done_ only after successful manual verification against acceptance criteria.

| User Story               | Description                             | Test Performed                                                                       | Result | Evidence                                                                        |
| ------------------------ | --------------------------------------- | ------------------------------------------------------------------------------------ | ------ | ------------------------------------------------------------------------------- |
| View home page           | User can view the landing page          | Loaded home page as anonymous and authenticated user                                 | Pass   | ![View screenshot](./documentation/features/home-anonymous.png)                 |
| Browse resources         | User can browse all published resources | Verified resource list shows only published items and currently auth'd user's drafts | Pass   | ![View screenshot](./documentation/features/browse-resources.png)               |
| View resource detail     | User can view a single resource         | Opened resource detail page via list and direct URL                                  | Pass   | ![View screenshot](./documentation/features/view-detail.png)                    |
| Security and permissions | Access restricted based on user role    | Tested access as anonymous, author, and non-author                                   | Pass   | ![View screenshot](./documentation/features/access-restricted.png)              |
| Login                    | User can log in                         | Logged in, verified session state                                                    | Pass   | ![View screenshot](./documentation/features/signed-in.png)                      |
| Logout                   | User can log out                        | Logged out, verified session state                                                   | Pass   | ![View screenshot](./documentation/features/logout.png)                         |
| Register account         | User can create an account              | Registered new user and verified login success                                       | Pass   | ![View screenshot](./documentation/features/new-signup-message.png)             |
| Validation and errors    | Errors shown for invalid actions        | Submitted invalid forms and checked error feedback                                   | Pass   | ![View screenshot](./documentation/features/message-error.png)                  |
| Admin manage content     | Admin can manage content                | Verified admin CRUD via Django admin                                                 | Pass   | ![View screenshot](./documentation/features/admin.png)                          |
| Delete comment           | User can delete own comment             | Deleted own comment; blocked deletion by other users                                 | Pass   | ![View screenshot](./documentation/features/comment-delete-confirm-desktop.png) |
| Edit resource            | Author can edit own resource            | Edited resource; verified updates persisted                                          | Pass   | ![View screenshot](./documentation/features/add-edit-resource-desktop.png)      |
| Add comment              | Logged-in user can add comments         | Added comment; verified display and association                                      | Pass   | ![View screenshot](./documentation/features/comment-form-desktop.png)           |
| Create resource          | Logged-in user can create a resource    | Created resource; verified saved as draft/published                                  | Pass   | ![View screenshot](./documentation/features/add-edit-resource-desktop.png)      |
| Delete resource          | Author can delete own resource          | Deleted resource; confirmed DB record removal                                        | Pass   | ![View screenshot](./documentation/features/delete-resources.png)               |
| Filter resources         | User can filter resources               | Applied filters and verified result set                                              | Pass   | ![View screenshot](./documentation/features/search-filter-resources.png)        |
| Search resources         | User can search for resources           | Performed keyword search and validated results                                       | Pass   | ![View screenshot](./documentation/features/search-filter-resources.png)        |
| Responsive design        | Site works across screen sizes          | Tested layouts on mobile, tablet, and desktop                                        | Pass   | see [Responsiveness](#responsiveness)                                           |

---

## Bugs

### Fixed Bugs

All identified bugs were logged and tracked using [**GitHub Issues**](https://github.com/yenmangu/ci-ms-3-studystack/issues). Issues were resolved incrementally with clear commit history.

Examples include:

- Incorrect slug handling during updates
- Subject duplication during resource edits
- Permission edge cases on delete views

> [!NOTE]
> See [Bugs](./README.md#development-bugs) for a comprehensive bugs report.
> Where applicable, GitHub Issues have been resolved with an accompanying screenshot to provide evidence.

---

### Unfixed Bugs

> [!IMPORTANT]
> There are no known unfixed bugs at the time of submission.
> To check, visit [**The GitHub Issues page**](https://github.com/yenmangu/ci-ms-3-studystack/issues).

![Screenshot](./documentation/agile/screenshots/no-open-issues.png)

---

## Known Issues

### TinyMCE console errors (third-party)

The project uses the TinyMCE plugin to provide a WYSIWYG editor for rich-text fields. During manual testing, browser developer tools displayed console errors originating from TinyMCE’s client-side scripts.

These errors:

- originate from third-party code,
- do not prevent content creation or editing,
- do not affect form submission or saved data,
- do not impact user-facing functionality.

#### Evidence

| Device | Screenshot                                                                                                  |
| ------ | ----------------------------------------------------------------------------------------------------------- |
| Mobile | ![TinyMCE console errors on mobile](./documentation/responsiveness/sizes/create-tiny_mce-errors-mobile.png) |
| Tablet | ![TinyMCE console errors on tablet](./documentation/responsiveness/sizes/create-tiny_mce-errors-tablet.png) |

---

## Summary

Testing demonstrates that **StudyStack** is:

- Functionally complete
- Secure against unauthorised actions
- Responsive and accessible
- Robust in handling invalid input
