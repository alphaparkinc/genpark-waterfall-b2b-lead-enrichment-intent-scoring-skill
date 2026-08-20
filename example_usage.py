from client import WaterfallB2BLeadEnrichmentIntentScoringClient

def main():
    client = WaterfallB2BLeadEnrichmentIntentScoringClient()
    res = client.enrich_prospect("acme-cloud.io", "Head of AI Infrastructure")
    print(f"ICP Fit Grade: {res['icp_fit_grade']}")
    print(f"Buyer Intent Score: {res['buyer_intent_score']}/100")
    print("Technographic Stack:", res["technographic_stack"])
    print("Enriched Contacts:", res["enriched_contacts"])

if __name__ == "__main__":
    main()
