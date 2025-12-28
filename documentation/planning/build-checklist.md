# StudyStack – Build Checklist

This checklist is used to track implementation progress against the planned Epics, User Stories, and MoSCoW priorities for the StudyStack project.

---

## Phase 1: Project Setup & Core Structure (Foundation)

- [x] Initial commit: project scaffold
- [x] Create Django project and main app
- [ ] Set up project structure (templates, static, media)
- [ ] Configure base template (`base.html`)
- [ ] Add navigation bar with conditional auth links
- [ ] Enable Django messages framework
- [ ] Configure environment variables (`SECRET_KEY`, `DEBUG`, DB config)

---

## Phase 2: Core Navigation & Site Purpose

**Epic 1 – Must Have**

- [ ] Create home page view
- [ ] Add site purpose and description (StudyStack)
- [ ] Add primary calls-to-action (Browse / Register / Login)
- [ ] Link navigation to key pages
- [ ] Update Feature Table:
  - View Home Page & Site Purpose → ✅

---

## Phase 3: Authentication & Account Management

**Epic 2 – Must Have**

- [ ] Implement user registration (sign-up)
- [ ] Implement login functionality
- [ ] Implement logout functionality
- [ ] Show login/logout state in navigation
- [ ] Add feedback messages for auth actions
- [ ] Protect restricted routes
- [ ] Update Feature Table:
  - User Registration → ✅
  - User Login & Logout → ✅

---

## Phase 4: Data Modelling & Admin Setup

**Foundation for CRUD**

- [ ] Create `Resource` model
- [ ] Create `Topic` model
- [ ] Set up Many-to-Many relationship (Resource ↔ Topic)
- [ ] Create `Comment` model
- [ ] Run migrations
- [ ] Register models in Django admin
- [ ] Add sample data via admin

---

## Phase 5: Resource Discovery (Read & Locate)

**Epic 3 – Must / Should / Could**

- [ ] Create resource list view
- [ ] Display resource cards with summary info
- [ ] Create resource detail view
- [ ] Display topics/tags on detail page
- [ ] Implement search functionality (keyword-based)
- [ ] Implement filter by topic and type
- [ ] Handle empty and no-result states
- [ ] Update Feature Table:
  - Browse Study Resources → ✅
  - View Resource Detail Page → ✅
  - Search Study Resources → ✅
  - Filter Resources by Topic & Type → ✅ (if implemented)

---

## Phase 6: Resource Contribution (Create)

**Epic 4 – Must Have**

- [ ] Create “Add Resource” form
- [ ] Restrict access to logged-in users
- [ ] Validate form inputs
- [ ] Save resource with owner reference
- [ ] Show success feedback on creation
- [ ] Update Feature Table:
  - Create Study Resource → ✅

---

## Phase 7: Resource Ownership & Management

**Epic 5 – Must Have**

- [ ] Implement edit resource view
- [ ] Restrict editing to resource owner
- [ ] Implement delete confirmation view
- [ ] Restrict deletion to resource owner
- [ ] Show success feedback for updates/deletions
- [ ] Update Feature Table:
  - Edit Own Study Resource → ✅
  - Delete Own Study Resource → ✅

---

## Phase 8: Community Interaction (Comments)

**Epic 6 – Should Have**

- [ ] Display comments on resource detail page
- [ ] Create add comment form (logged-in users only)
- [ ] Save comment with owner reference
- [ ] Implement delete comment functionality
- [ ] Restrict deletion to comment owner
- [ ] Update Feature Table:
  - Add Comment to Resource → ✅
  - Delete Own Comment → ✅

---

## Phase 9: Validation, Feedback & Error Handling

**Epic 8 – Must Have**

- [ ] Add form-level validation messages
- [ ] Preserve user input on form errors
- [ ] Handle invalid URLs and missing resources
- [ ] Add custom 404 page
- [ ] Prevent unauthorised actions gracefully
- [ ] Update Feature Table:
  - Form Validation & Error Feedback → ✅

---

## Phase 10: Responsive Design & Accessibility

**Epic 9 – Must Have**

- [ ] Apply responsive layout (mobile-first)
- [ ] Test layouts on mobile, tablet, desktop
- [ ] Ensure readable typography and spacing
- [ ] Check colour contrast and focus states
- [ ] Update Feature Table:
  - Responsive Design → ✅

---

## Phase 11: Security & Permissions

**Epic 10 – Must Have**

- [ ] Ensure all secrets stored in environment variables
- [ ] Disable `DEBUG` in production
- [ ] Restrict create/edit/delete to authenticated users
- [ ] Enforce owner-only permissions
- [ ] Test permission edge cases
- [ ] Update Feature Table:
  - Security & Permissions Enforcement → ✅

---

## Phase 12: Testing, Documentation & Deployment

- [ ] Manual testing of all user stories
- [ ] Document testing results
- [ ] Fix or document known bugs
- [ ] Finalise README
- [ ] Deploy to production (Heroku)
- [ ] Verify deployed version matches local
- [ ] Final review of Feature Table (all Must-Have = ✅)

---
