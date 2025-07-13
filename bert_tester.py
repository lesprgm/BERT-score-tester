from bert_score import score

llm_generated_text = """GOOGLE TECHNICAL PHONE INTERVIEW PREPARATION GUIDE
For: Rising Junior Candidate
=====================================================

INTERVIEW FORMAT (45-60 minutes)
- 5 minutes: Brief introductions
- 35-40 minutes: Coding/problem-solving
- 5-10 minutes: Your questions for interviewer
- Conducted via Google Meet with shared coding environment

KEY TECHNICAL AREAS TO MASTER
=====================================================

1. DATA STRUCTURES
Essential proficiency required in:
- Arrays & Strings
- Hash Tables/Maps
- Linked Lists
- Trees (especially Binary Trees & BST)
- Graphs
- Stacks & Queues

2. ALGORITHMS
Focus areas:
- Binary Search
- DFS/BFS
- Tree/Graph Traversal
- Sorting (especially Quick Sort and Merge Sort)
- Two Pointer Technique
- Sliding Window
- Dynamic Programming (basic)

3. COMPLEXITY ANALYSIS
Must be able to:
- Analyze time & space complexity
- Explain trade-offs between solutions
- Optimize initial solutions

EXAMPLE QUESTION TYPES
=====================================================
1. String/Array Manipulation:
   "Given a string, find the length of longest substring without repeating characters"

2. Tree Operations:
   "Determine if a binary tree is balanced"

3. Graph Problems:
   "Find the shortest path between two nodes in an unweighted graph"

STUDY MATERIALS
=====================================================
1. Essential Resources:
   - LeetCode (focus on Medium difficulty)
   - "Cracking the Coding Interview" book
   - Google Tech Dev Guide (online)

2. Practice Plan:
   Week 1-2: Data Structures fundamentals
   Week 3-4: Algorithms & Problem-solving patterns
   Week 5-6: Mock interviews & timing practice

INTERVIEW DAY PROTOCOL
=====================================================
1. Before Interview:
   - Test your audio/video/internet
   - Have paper/pen ready
   - Choose a quiet location
   - Have water nearby

2. During Problem-Solving:
   - Think aloud
   - Start with clarifying questions
   - Discuss approach before coding
   - Consider edge cases
   - Test your solution

EVALUATION CRITERIA
=====================================================
We assess:
1. Problem-solving approach
2. Coding fluency
3. Testing methodology
4. Communication skills
5. Time management

KEY SUCCESS BEHAVIORS
=====================================================
DO:
- Ask clarifying questions
- Explain your thought process
- Consider multiple approaches
- Write clean, readable code
- Test your solution

DON'T:
- Jump straight to coding
- Stay silent while thinking
- Ignore edge cases
- Submit untested code

PRACTICE CHECKLIST
=====================================================
Daily:
□ 1-2 LeetCode problems
□ Implement 1 data structure from scratch
□ Review time/space complexity

Weekly:
□ 2-3 mock interviews
□ Review previous solutions
□ Practice explaining solutions verbally

FINAL TIPS
=====================================================
1. Code Quality Matters:
   - Use meaningful variable names
   - Write modular code
   - Handle edge cases
   - Add comments for clarity

2. Communication is Key:
   - Explain your approach
   - Ask questions
   - Think aloud
   - Be receptive to hints

3. Time Management:
   - Aim to have working solution in 20-25 minutes
   - Leave time for optimization
   - Reserve time for testing

Remember: We're looking for problem-solving ability and potential, not just memorized solutions. Focus on understanding patterns and approaches rather than memorizing specific solutions.

Good luck with your preparation! Feel free to reach out if you need clarification on any points.

[End of Guide]
"""

reference_text = """2.1.2 Google online assessment (90 minutes) - new graduates and interns only

If you're applying for a new graduate or intern position your process will often start with a coding sample test to take online. The coding sample includes two questions that you have to complete in less than 90 minutes in total.

The questions are similar to the ones you'll be asked in your interviews (i.e. data structures and algorithms). Note that you'll need to write your own test cases as you won't be provided with any. You can do that in your own IDE before submitting your solution. To pass to the next round you usually need to solve both of the questions correctly.

Check out the archives of coding competitions Google organizes to get an idea of the type of questions you'll come across. We recommend looking at the Code Jam competition in particular. Leetcode also maintains a thread on what questions to expect in Google's sample coding test. You can also find a list of preparation tips in our Google online assessment guide.

2.1.3 Technical phone screen

If you're an experienced hire, or if you are a new graduate who has passed the coding sample test, you'll be invited to one or two technical phone screens. This step is called the "phone screen", but most of the time it takes place over video chat on Google Hangouts / Google Meet. Each interview will last 30 to 60 minutes. You'll speak to a peer or a potential manager and they'll ask you to solve data structure and algorithm questions.

You'll share a Google Doc with your interviewer, write your solution directly in the document and won't have access to syntax highlighting or auto-completion like you would in a regular IDE. It's therefore a good idea to practice writing code in Google Docs before your interview.

Finally, in addition to coding questions, you should also be ready to answer a few typical behavioral questions including "Tell me about yourself," "Why Google?" or, "Tell me about a recent project you worked on." These questions are less frequent than they are in engineering interviews at Facebook or Amazon but it's still a good idea to think through the main ones ahead of time.

2.1.4 Onsite interviews

Onsite interviews are the real test. You'll typically spend a full day at a Google office and do four to six interviews in total. Each interview will last about 45 minutes and cover one of the following topics:

Coding interviews
System design interviews (Level 5 and above)
Leadership interviews (management positions only)
You'll typically get three coding interviews with data structure and algorithm questions, and one or two system design interviews if you're level 5 or above. If you're applying for a leadership role like the engineering manager position, you'll be given the option to choose between coding and code review for your technical round.

For more information about how Google conducts its system design and coding interviews, take a look at our Google system design interview guide and Google coding interview guide.

You'll use a whiteboard to write your code in most onsite interviews at Google. But the company has also started offering Chromebooks for coding interviews at some locations. These laptops come with an interview app that lets you choose the coding language you want to use.

In addition, if you're applying for a management position (e.g. Engineering Manager) then you'll also have leadership interviews where you'll be asked behavioral questions about leading teams and projects.

Finally, in addition to interviews, you'll also have lunch with a fellow engineer while you are onsite. The lunch interview is meant to be your time to ask questions about what it's like to work at Google. The company won't be evaluating you during this time, but we recommend that you behave as if they are.
Google software engineers solve some of the most difficult problems the company faces with code. It's therefore essential that they have strong problem-solving skills. This is the part of the interview where you want to show that you think in a structured way and write code that's accurate, bug-free, and fast.

Here are the most common question types asked in Google coding interviews and their frequency. Please note the list below excludes system design and behavioral questions, which we'll cover later in this article.

Graphs / Trees (39% of questions, most frequent)
Arrays / Strings (26%)
Dynamic programming (12%)
Recursion (12%)
Geometry / Maths (11% of questions, least frequent)
Below, we've listed common examples used at Google for each of these different question types. To make these questions easier to study, we've modified the phrasing to match the closest problem on Leetcode or another resource, and we've linked to a free solution.

Finally, we recommend reading this guide on how to answer coding interview questions and practicing with this list of coding interview examples in addition to those listed below.

Example Google coding interview questions

1. Graphs / Trees (39% of questions, most frequent)

"Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree." (Solution)
"Given an encoded string, return its decoded string." (Solution)
"We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5, and 7 are rotated 180 degrees, they become invalid. A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.) Given a positive integer N, return the number of confusing numbers between 1 and N inclusive." (Solution)
"Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that: 1) Only one letter can be changed at a time and, 2) Each transformed word must exist in the word list." (Solution)
"Given a matrix of N rows and M columns. From m[i][j], we can move to m[i+1][j], if m[i+1][j] > m[i][j], or can move to m[i][j+1] if m[i][j+1] > m[i][j]. The task is print longest path length if we start from (0, 0)." (Solution)
"Given a robot cleaner in a room modeled as a grid. Each cell in the grid can be empty or blocked. The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees. When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell. Design an algorithm to clean the entire room using only the 4 given APIs shown below." (Solution)
2. Arrays / Strings (26%)

Implement a SnapshotArray that supports pre-defined interfaces (note: see link for more details). (Solution)
"In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.) We may rotate the i-th domino, so that A[i] and B[i] swap values. Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same. If it cannot be done, return -1." (Solution)
"Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times. You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed." (Solution)
"Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n)." (Solution)
"Given a list of query words, return the number of words that are stretchy." Note: see link for more details. (Solution)
"Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified." (Solution)
3. Dynamic Programming (12%)

"Given a matrix and a target, return the number of non-empty submatrices that sum to target." (Solution)
"Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area." (Solution)
"Your car starts at position 0 and speed +1 on an infinite number line. (Your car can go into negative positions.) Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse)...Now for some target position, say the length of the shortest sequence of instructions to get there." (Solution)
"Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W. If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index." (Solution)
4. Recursion (12%)

"A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down). Find all strobogrammatic numbers that are of length = n." (Solution)
"Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root. The length of path between two nodes is represented by the number of edges between them." (Solution)
"Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive). The binary search tree is guaranteed to have unique values." (Solution)
5. Geometry / Math (11% of questions, least frequent)

"A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|." (Solution)
"You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list." (Solution)
What type of coding questions are asked in Google interviews?

Google software engineer interviews include a range of coding questions that assess your problem-solving skills, algorithmic understanding, and coding proficiency. Google asks questions that will test your knowledge of key data structures such as graphs, trees, arrays, or strings. Also, expect some algorithmic problems around dynamic programming, matrix, targets, and recursion.
4. Google Interviewing Tips ↑

You might be a fantastic software engineer, but unfortunately, that’s not necessarily enough to ace your interviews at Google. Interviewing is a skill in itself that you need to learn. 

Let’s look at some key tips to make sure you approach your interviews in the right way.  

4.1 Ask clarifying questions

Often, the questions you’ll be asked will be ambiguous, so make sure you ask questions that can help you clarify and understand the problem. 

4.2 Think out loud

You need to walk your interviewer through your thought process before you actually start coding or designing a system.  Your interviewer may give you hints about whether you’re on the right track or not. 

4.3 State and check assumptions

You need to explicitly state assumptions and check with your interviewer to see if those assumptions are reasonable. 

4.4 Be honest and authentic

Be genuine in your responses. Google interviewers appreciate authenticity and honesty. If you faced challenges or setbacks, discuss how you improved and learned from them.

4.5 Center on Google’s values

Familiarize yourself with Google’s core values and align your behavioral responses with them. Google values certain attributes such as passion for technology, collaboration, and focus on the user.

4.6 Practice system design

Even more than with coding problems, answering system design questions is a skill in itself. You should start with a high-level design and then drill down on the system component of the design. Use our Google system design interview guide to prepare. 

4.7 Brute force, then iterate.

When coding, don’t necessarily go for the perfect solution straight away. Google recommends that you first try and find a solution that works as quickly as you can, then iterate to refine your answer.

4.8 Get comfortable with coding on various mediums

Google now typically asks interviewees to code in a Google doc. But this can vary, it could be on a physical whiteboard or a virtual one. Check with your recruiter what it will be and practice it a lot. 

The key is to keep your code organized so your interviewer won’t have a hard time understanding what you’ve written. 

4.9 Master at least one of the recommended programming languages

You will be asked to code so make sure you’ve mastered at least one programming language. Google recommends these languages: C++, C, Python, Java, or Go. 
"""


candidates = [llm_generated_text]
references = [reference_text]

# A score closer to 1 means high similarity, closer to -1 means high dissimilarity to the reference text
P, R, F1 = score(candidates, references, lang="en", rescale_with_baseline=False) 

print(f"BERTScore Precision (Raw): {P[0]:.4f}")
print(f"BERTScore Recall (Raw): {R[0]:.4f}")
print(f"BERTScore F1 (Raw): {F1[0]:.4f}")