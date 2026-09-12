---
name: Clinical Intelligence
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#45464d'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#0051d5'
  on-secondary: '#ffffff'
  secondary-container: '#316bf3'
  on-secondary-container: '#fefcff'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#0b1c30'
  on-tertiary-container: '#75859d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#dbe1ff'
  secondary-fixed-dim: '#b4c5ff'
  on-secondary-fixed: '#00174b'
  on-secondary-fixed-variant: '#003ea8'
  tertiary-fixed: '#d3e4fe'
  tertiary-fixed-dim: '#b7c8e1'
  on-tertiary-fixed: '#0b1c30'
  on-tertiary-fixed-variant: '#38485d'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-padding-mobile: 20px
  container-padding-desktop: 40px
  gutter: 24px
  section-gap: 64px
  element-gap: 16px
---

## Brand & Style

This design system is engineered for a high-end medical AI context, specifically tailored for dermatology and skin health. The brand personality is authoritative, calm, and meticulously precise. It prioritizes clarity and clinical trust over decorative flair, ensuring that patients and practitioners feel a sense of security and professional oversight.

The aesthetic follows a **Modern Corporate** approach with a strong emphasis on **Minimalism**. It utilizes expansive white space to reduce cognitive load, suggesting an environment of cleanliness and efficiency. Visual hierarchy is established through disciplined typography and a restricted color palette, ensuring the AI-driven data remains the primary focus. The emotional response should be one of "digital sterilization"—clean, organized, and reliable.

## Colors

The palette is anchored in high-contrast professional tones to ensure maximum legibility and a sense of "Medical Grade" quality.

- **Primary (Deep Navy):** Reserved for high-level headings, brand elements, and primary text. It provides the "weight" and authority of a traditional medical institution.
- **Accent (Medical Blue):** Used exclusively for primary calls-to-action, active states, and critical interactive elements. It signifies clinical precision.
- **Secondary (Slate Gray):** Utilized for secondary information, metadata, and supporting icons to maintain a quiet visual hierarchy.
- **Surfaces (Pale Blue/White):** The background is pure white (#FFFFFF) to maintain a clinical feel, while interactive cards and containers use Pale Blue (#F8FAFC) to create soft, legible boundaries without the harshness of heavy borders.

## Typography

This design system utilizes **Inter** for its systematic, utilitarian, and highly legible qualities. The typeface’s large x-height and neutral character make it ideal for reading medical reports and AI analysis.

- **Headlines:** Set in Deep Navy with tighter letter spacing for a confident, editorial look.
- **Body Text:** Optimized for long-form reading with generous line heights to prevent visual fatigue.
- **Labels:** Used for metadata, data visualization markers, and small captions. These often use a slightly heavier weight (Medium/Semi-bold) to ensure visibility at small sizes.
- **Scaling:** On mobile devices, large headlines scale down to prevent awkward word breaks, maintaining a maximum size of 28px for primary headers.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** approach for desktop and a **Fluid Content** approach for mobile to maintain the integrity of medical data displays.

- **Desktop:** A 12-column grid with a max-width of 1280px. Gutters are fixed at 24px to provide "breathing room" between complex data widgets.
- **Mobile:** A single-column flow with 20px side margins. 
- **Rhythm:** An 8px linear scale governs all spacing. Vertical rhythm is generous; components are separated by 16px (element-gap) or 64px (section-gap) to evoke a sense of calm and prevent the UI from feeling "crowded," which can cause anxiety in medical contexts.

## Elevation & Depth

To maintain a "clinical" and "flat" professional feel, this design system avoids heavy, dramatic shadows. Instead, it uses **Low-contrast outlines** and **Tonal layers**.

- **Level 0 (Background):** Pure White (#FFFFFF).
- **Level 1 (Cards/Surface):** Pale Blue (#F8FAFC) with a subtle 1px border in a slightly darker slate (#E2E8F0). 
- **Level 2 (Interactive Elements):** On hover or interaction, elements may use an **Ambient Shadow**: a very diffused, 10% opacity Deep Navy shadow (0px 4px 20px) to suggest "lift" without breaking the clean aesthetic.
- **Backdrop:** For modals or AI scanning overlays, a light backdrop blur (8px) is used over a semi-transparent white wash to keep the focus on the foreground medical data.

## Shapes

The shape language is defined by large, friendly, yet professional radii. While the brand is clinical, the skin is organic; therefore, sharp corners are avoided to make the app feel more "human" and less "industrial."

- **Standard Components:** Buttons and inputs use a 0.5rem (8px) radius.
- **Containers & Cards:** Primary surface containers (e.g., patient records, AI results) use a **Large** radius of 1rem (16px) or **Extra Large** 1.5rem (24px) for prominent dashboard widgets.
- **Icons:** Icons should be enclosed in circular or highly rounded square containers to maintain the soft-professional balance.

## Components

- **Buttons:** Primary buttons are Medical Blue (#2563EB) with white text, utilizing the "Rounded" (8px) corner spec. Secondary buttons use a ghost style with a Slate Gray border.
- **AI Result Cards:** Feature a 16px corner radius, #F8FAFC background, and a subtle #E2E8F0 border. They should include a "Confidence Score" chip in the top right.
- **Input Fields:** Use a white background to contrast against #F8FAFC surfaces, with a 1px border that turns Medical Blue on focus.
- **Chips/Badges:** Small, pill-shaped indicators for status (e.g., "Review Required," "Stable"). Use low-saturation background tints with high-saturation text.
- **Iconography:** Line-based icons with a 2px stroke width. Use professional metaphors: a Shield for privacy/security, a Camera for skin capture, and a Pulse/Stethoscope for general health.
- **AI Scanning View:** A dedicated component featuring a centered camera viewfinder with a pulsating Medical Blue border to indicate active AI analysis.