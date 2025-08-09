def build_prompt(course_info, question):
    return f"""
You are a helpful course assistant. Use the following course details to answer the student's question.

Course Info:
- Title: {course_info['title']}
- Start Date: {course_info['start_date']}
- Duration: {course_info['duration']}
- Payment: {course_info['payment']}
- Certificate: {course_info['certificate']}

Student Question:
{question}

Respond in a polite and informative way.
"""
