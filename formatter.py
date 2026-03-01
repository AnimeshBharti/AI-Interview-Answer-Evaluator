def display_result(result):
    print("\n----Interview Evaluation Result----")

    print(f"Technical Accuracy: {result['technical_accuracy']}/25")
    print(f"Clarity: {result['clarity']}/15")
    print(f"Structure: {result['structure']}/10")
    print(f"Depth: {result['depth']}/25")
    print(f"Communication: {result['communication']}/25")

    print("\nStrengths:")
    for point in result["strength"]:
        print(f"  - {point}")

    print("\nWeaknesses:")
    for point in result["weakness"]:
        print(f"  - {point}")

    print("\nSuggestions:")
    for point in result["suggestions"]:
        print(f"  - {point}")


    print(f"\nOverall Interview Score: {result['overall_interview_score']}/100")