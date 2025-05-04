def predict_course(age, gender, interest):
    interest = interest.lower()
    gender = gender.lower()

    if "tech" in interest or "computer" in interest or "it" in interest or "programming" in interest:
        return "Computer Science"
    elif "business" in interest or "marketing" in interest or "entrepreneur" in interest:
        return "Business Administration"
    elif "art" in interest or "design" in interest or "creative" in interest:
        return "Fine Arts"
    elif "health" in interest or "nursing" in interest or "medical" in interest:
        return "Nursing"
    elif "engineering" in interest:
        return "Engineering"
    elif "education" in interest or "teaching" in interest:
        return "Education"

    if gender == "female" and age < 20:
        return "Education"
    elif gender == "male" and age < 20:
        return "Information Technology"

    return "General Studies"