class WaterfallB2BLeadEnrichmentIntentScoringClient:
    def enrich_prospect(self, company_domain: str, target_persona_title: str = "VP of Engineering") -> dict:
        contacts = [
            {"full_name": "Sarah Chen", "title": "VP of Engineering", "verified_email": "sarah@acme-cloud.io", "linkedin_url": "https://linkedin.com/in/sarahchen"}
        ]
        return {
            "enriched_contacts": contacts,
            "technographic_stack": ["PostgreSQL", "Kubernetes", "Next.js", "Stripe", "Claude API"],
            "buyer_intent_score": 92.0,
            "icp_fit_grade": "TIER_1_ENTERPRISE_FIT"
        }
