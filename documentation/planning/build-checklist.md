# StudyStack – Build Checklist

This checklist is used to track implementation progress against the planned Epics, User Stories, and MoSCoW priorities for the StudyStack project.

---

## Phase 1: Project Setup & Core Structure (Foundation)

- [x] Initial commit: project scaffold
- [x] Create Django project and main app
- [x] Set up project structure (templates, static, media)
- [x] Set up minimal view
- [x] Configure base template (`base.html`)
- [x] Add navigation bar with conditional auth links
- [x] Enable Django messages framework
- [x] Configure environment variables (`SECRET_KEY`, `DEBUG`, DB config)

---

## Phase 2: Core Navigation & Site Purpose

**Epic 1 – Must Have**

- [x] Create home page view
- [x] Add site purpose and description (StudyStack)
- [x] Add primary calls-to-action (Browse / Register / Login)
- [x] Link navigation to key pages
- [x] Update Feature Table:
  - View Home Page & Site Purpose → ✅

---

## Phase 3: Authentication & Account Management

**Epic 2 – Must Have**

- [x] Implement user registration (sign-up)
- [x] Implement login functionality
- [x] Implement logout functionality
- [x] Show login/logout state in navigation
- [x] Add feedback messages for auth actions
- [x] Protect restricted routes
- [x] Update Feature Table:
  - User Registration → ✅
  - User Login & Logout → ✅

---

## Phase 4: Data Modelling & Admin Setup

**Foundation for CRUD**

- [x] Create `Resource` model
- [x] Create `Topic` model
- [x] Set up Many-to-Many relationship (Resource ↔ Topic)
- [x] Create `Comment` model
- [x] Run migrations
- [x] Register models in Django admin
- [x] Add sample data via admin

---

## Phase 5: Resource Discovery (Read & Locate)

**Epic 3 – Must / Should / Could**

- [x] Create resource list view
- [x] Display resource cards with summary info
- [x] Create resource detail view
- [x] Display topics/tags on detail page
- [x] Implement search functionality (keyword-based)
- [x] Implement filter by topic and type
- [x] Handle empty and no-result states
- [x] Update Feature Table:
  - Browse Study Resources → ✅
  - View Resource Detail Page → ✅
  - Search Study Resources → ✅
  - Filter Resources by Topic & Type → ✅ (if implemented)

---

## Phase 6: Resource Contribution (Create)

**Epic 4 – Must Have**

- [x] Create “Add Resource” form
- [x] Restrict access to logged-in users
- [x] Validate form inputs
- [x] Save resource with owner reference
- [x] Show success feedback on creation
- [x] Update Feature Table:
  - Create Study Resource → ✅

---

## Phase 7: Resource Ownership & Management

**Epic 5 – Must Have**

- [x] Implement edit resource view
- [x] Restrict editing to resource owner
- [x] Implement delete confirmation view
- [x] Restrict deletion to resource owner
- [x] Show success feedback for updates/deletions
- [x] Update Feature Table:
  - Edit Own Study Resource → ✅
  - Delete Own Study Resource → ✅

---

## Phase 8: Community Interaction (Comments)

**Epic 6 – Should Have**

- [x] Display comments on resource detail page
- [x] Create add comment form (logged-in users only)
- [x] Save comment with owner reference
- [x] Implement delete comment functionality
- [x] Restrict deletion to comment owner
- [x] Update Feature Table:
  - Add Comment to Resource → ✅
  - Delete Own Comment → ✅

---

## Phase 9: Validation, Feedback & Error Handling

**Epic 8 – Must Have**

- [x] Add form-level validation messages
- [x] Preserve user input on form errors
- [x] Handle invalid URLs and missing resources
- [x] Add custom 404 page
- [x] Prevent unauthorised actions gracefully
- [x] Update Feature Table:
  - Form Validation & Error Feedback → ✅

---

## Phase 10: Responsive Design & Accessibility

**Epic 9 – Must Have**

- [x] Apply responsive layout (mobile-first)
- [x] Test layouts on mobile, tablet, desktop
- [x] Ensure readable typography and spacing
- [x] Check colour contrast and focus states
- [x] Update Feature Table:
  - Responsive Design → ✅

---

## Phase 11: Security & Permissions

**Epic 10 – Must Have**

- [x] Ensure all secrets stored in environment variables
- [x] Disable `DEBUG` in production
- [x] Restrict create/edit/delete to authenticated users
- [x] Enforce owner-only permissions
- [x] Test permission edge cases
- [x] Update Feature Table:
  - Security & Permissions Enforcement → ✅

---

## Phase 12: Testing, Documentation & Deployment

- [x] Manual testing of all user stories
- [x] Document testing results
- [x] Fix or document known bugs
- [x] Finalise README
- [x] Deploy to production (Heroku)
- [x] Verify deployed version matches local
- [x] Final review of Feature Table (all Must-Have = ✅)

---
