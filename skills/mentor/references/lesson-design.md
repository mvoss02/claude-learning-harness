# Measure, then design, then write

Added 2026-11-02 after a lab README that started in the middle: it assumed a floor nobody had measured and read as a cheat sheet. Two rules follow. No lesson text before a measured floor. No lesson text before a written design.

## 1. Measure: the probe

Ten minutes, before the lesson, by voice if the learner has it. Goal: for each strand the lesson depends on, one thing the learner reliably gets right (the floor) and one they get wrong or do not know (the ceiling). The lesson starts at the floor.

- **Ledger first.** A strand with a card at `practiced` or above, or demonstrated in a recent build, is not re-probed. Evidence beats questions.
- **Strands** are the three to six things the objective rests on. For "read a file in C": what a program is to the kernel, the syscall boundary, file descriptors, memory you own (buffers, pointers), the return contract of a call, error reporting.
- **Enter near the top.** An engineer reaching for this material holds the basics; open each strand near the hardest thing the lesson needs and let a miss walk down. Opening at textbook level wastes the question.
- **One question at a time.** The next question is chosen from the last answer. Correct and confident: jump up. Correct but hesitant: one step up, note the fragility. Wrong: narrow in. A strand that never breaks is not done; escalate until it breaks or the ceiling is above the lesson's needs.
- **Every answer carries two things:** a confidence number (0 to 100, said before the verdict) and the reasoning out loud. Wrong plus high confidence is a committed misconception and the most valuable finding of the probe. Right plus low confidence is fragile and gets a re-ask later. A right answer on confused reasoning counts as a miss.
- **Nothing is graded.** Say so. A miss is a coordinate, not a verdict.
- **Record** per strand: floor, ceiling, confidence pattern, one line of what the learner said, and any misconception verbatim. Goes in the journal and into the design below. Misconceptions also go to the mistake log in the learner's words.

## 2. Design: the chain

Written before any lesson text, kept with the mentor's private notes. One page.

1. **Objective.** One sentence of what the learner can do afterwards, and the interview question it answers.
2. **Floor.** Per strand, from the probe: what is held, what is not. Two lines each.
3. **Chain.** The shortest ordered list of concepts from the floor to the objective. Per concept: the problem it solves (as a situation in this system), the artifact the mechanism is shown on, the worked example (unrelated content), the check (say-back or completion, never cold), the exercise or lab stage that uses it, and the one unknown it carries. A concept with two unknowns is two concepts. Where the learner's baseline language gives the wrong answer here, one interference line ("in Python X; here Y").
4. **Cuts and neighbours.** What was deliberately left out and why. Related is not a reason to include; being on the path is. Neighbours worth a name (the thing the chain concept is easy to confuse with) get one sentence in the text, never a treatment.
5. **Expected misses.** For each check and each later recap question: the miss and the wrong model it reveals, so a miss can be diagnosed instead of counted.

Test of a design: cover the objective and read the chain backwards. Each concept should be required by the one after it. A concept nothing depends on is a cut.

## 3. Write

Only now the lesson text, in the order of the chain, one concept per screen, each at textbook depth (SKILL.md "Explaining"), with its check named and unanswered. "Where you start" at the top in two lines, from the floor. A long chain is split into two lessons, never compressed. The text never contains the answer to its own checks or to the exercise.
