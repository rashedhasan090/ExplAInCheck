# ExplAInCheck
Real-Time AI Explanation Verifier for Sensitive Decisions - CornHacks 2025 Project

## Overview

In an era where artificial intelligence increasingly influences critical decisions—from medical diagnoses to agricultural planning, financial advice to dietary recommendations—there's a growing concern: **How can we trust AI explanations when they affect our health, safety, and livelihood?**

ExplAInCheck addresses this challenge by creating the world's first real-time AI explanation verification system. When an AI system provides you with a recommendation or decision, ExplAInCheck doesn't just accept it at face value. Instead, it automatically parses the explanation into logical components, verifies each claim for consistency and completeness, and flags potential gaps, contradictions, or unsubstantiated assumptions.

## The Problem

AI systems today can generate impressively detailed explanations, but they often:
- Make logical leaps without justification
- Include hidden assumptions that may not apply to your situation
- Contradict themselves across different parts of the explanation
- Omit critical information needed for safe decision-making
- Present unverified claims as established facts

For sensitive domains like healthcare, agriculture, and nutrition, these gaps can have serious consequences. Yet most users lack the technical expertise to identify these issues.

## Our Solution

ExplAInCheck bridges the gap between AI-generated explanations and trustworthy decision-making through:

1. **Intelligent Parsing**: Using advanced NLP and formal language theory, we break down AI explanations into discrete logical statements and reasoning steps.

2. **Formal Verification**: We apply symbolic reasoning and constraint-solving techniques (SAT/SMT solvers) to verify the logical consistency of each step.

3. **Gap Detection**: Our system identifies missing premises, circular reasoning, and unsubstantiated claims that could undermine the explanation's validity.

4. **Interactive Debugging**: Users can click on any part of an explanation to understand why it's valid, questionable, or potentially unsafe—with clear, non-technical feedback.

5. **Domain-Aware Analysis**: Special attention to sensitive domains where AI mistakes matter most, including nutrition (featuring potassium tracking for the BANANAHACKS theme!), agriculture, and health.

## Why It Matters

This project represents a novel convergence of:
- **Generative AI** (understanding natural language explanations)
- **Formal methods** (mathematical verification of logical correctness)
- **AI Safety** (protecting users from harmful or misleading AI outputs)
- **Accessibility** (making verification tools usable by non-experts)

No existing platform offers real-time, interactive verification of AI explanations for end users. ExplAInCheck empowers individuals and communities to confidently use AI tools while maintaining critical oversight over decisions that affect their lives.

## CornHacks 2025 Demo

For this hackathon, we're focusing on agricultural and nutritional AI advice—perfectly aligned with the BANANAHACKS theme! Submit a dietary plan, farming schedule, or health recommendation from any AI system, and watch ExplAInCheck verify it in real-time, highlighting which claims are solid and which need your attention.

---

**Built for CornHacks 2025 | Presented by Conagra Brands**
