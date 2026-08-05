<h1 align="center">Oluwatobi Wilfred Ojulari</h1>

<p align="center">
  <b>Bioinformatics Data Engineer</b> · Toronto, ON
</p>

<p align="center">
  MS Bioinformatics @ Northeastern · BSc Computer Science, UNBC<br>
  I build reproducible genomics pipelines and the production backends that feed them.
</p>

<p align="center">
  <a href="https://oluwatobiojulari.netlify.app/"><img src="https://img.shields.io/badge/Portfolio-0A0A0A?style=for-the-badge&logo=netlify&logoColor=00C7B7" alt="Portfolio"></a>
  <a href="mailto:ojulari1@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://linkedin.com/in/YOUR-HANDLE"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
</p>

---

## How I got here

I started in general software engineering — three backend roles building REST APIs in Java,
Node, and Python, shipping auth systems, task queues, and relational schemas that had to survive
real users. Then I went deep on computational biology at Northeastern, and found that the hard
problems in genomics are mostly *data engineering* problems wearing a lab coat: workflow
orchestration, container reproducibility, scheduler contention, memory profiling, and provenance
you can actually defend.

That's the intersection I work at now. I'm not a biologist who picked up Python, and I'm not an
engineer who read a genomics tutorial — I write the pipelines *and* the platforms they run on.

**Currently:** finishing my MS in Bioinformatics and looking for bioinformatics data engineering
roles where pipeline rigor and backend craft both matter.

---

## Featured work

### 🧬 Bioinformatics & HPC

**[Reads2genome-HPC-Reproducibility](https://github.com/tobioj/Reads2genome-HPC-Reproducibility)**
Independently reproduced the Arcadia-Science `reads2genome` Nextflow pipeline on Northeastern's
Explorer SLURM cluster — 24 PacBio HiFi bacterial genomes through a 142-task workflow
(BAM→FASTQ, Flye assembly, BUSCO, Minimap2, MultiQC).

- **95.1%** first-attempt task success; 7 transient failures auto-recovered to 100% completion
- **93× parallelization speedup** — 47.8 CPU-hours in 31 minutes wall-clock
- Diagnosed and fixed **5 undocumented gaps** between the published docs and real HPC constraints, including patching `pacbio.nf` to run BUSCO's `bacteria_odb10` fully offline
- Assembly quality: **95.3% ± 2.8%** BUSCO completeness, **97.2% ± 2.1%** mapping rate, N50 ≈ 850 kb

`Nextflow DSL2` `SLURM` `Singularity/Apptainer` `Docker` `Flye` `BUSCO` `Minimap2` `MultiQC` `Bash`

> The interesting result wasn't that it reproduced — it's the five things that had to be fixed before it could.

---

### 🏗️ Full-stack platforms

**FindIt-V3 — Multi-Tenant Lost & Found Platform**
Multi-tenant event platform with role-based access control, guest reporting, and an immutable
audit trail on every status transition. The core is a custom matching engine scoring candidates
across three signals: Haversine geospatial proximity decay, Jaccard similarity over tokenized
text, and `difflib` fuzzy matching for brand classification. Celery + Redis run the async
matchmaking, event-scoped report expiry, and transactional email. Includes a dynamic
dealbreaker-penalty layer, a match-resurrection state machine for dismissed matches, and a pytest
suite covering every state transition.

`Django REST` `React` `Celery` `Redis` `PostgreSQL` `pytest`

**Automated Messaging Platform (AMS)**
Occasion-based scheduled messaging (birthdays, anniversaries) with admin approval/rejection
workflows, OAuth2 + JWT auth, role-based access control, and Twilio SMS delivery. Built during my
Junior Developer role at Chert System Solutions.

`FastAPI` `SQLAlchemy` `PostgreSQL` `Twilio` `OAuth2/JWT`

**[Homelab-Control-Plane](https://github.com/tobioj/Homelab-Control-Plane)**
Self-hosted PaaS that provisions Django apps end to end on a bare-metal server — systemd units,
nginx vhosts, Redis, Let's Encrypt DNS-01 certs, and observability. Every privileged action is
previewed as a diff before it executes.

`Python` `Django` `Linux` `nginx` `systemd`

---

### 📊 Data & ML pipelines

Side projects, but the same discipline: leakage-safe feature engineering, honest calibration, and
benchmarking against a real baseline instead of a flattering one.

**[UFC-MMA-Predictor](https://github.com/tobioj/UFC-MMA-Predictor)** — ML fight predictor with a
FastAPI + vanilla-JS analytics dashboard. Leakage-safe pipeline, calibrated ~62% accuracy,
benchmarked against the betting market. `Python` `FastAPI` `scikit-learn`

**[COD-Esport-Predictor](https://github.com/tobioj/COD-Esport-Predictor)** — Roster-aware CDL /
Esports World Cup 2026 predictor: mode-calibrated map & series odds, player kill-prop
projections, 20k-run Monte-Carlo bracket sim. `Python` `FastAPI` `Monte-Carlo`

**[Forex-Quant-Research](https://github.com/tobioj/Forex-Quant-Research)** — A forex EA taken from
hypothesis to out-of-sample failure. Public *because* the edge didn't hold — real-tick
backtesting, diagnostics, and the discipline to disprove your own idea. `Python` `MQL5`

---

## Toolkit

| | |
|---|---|
| **Languages** | Python · Bash/Shell · Nextflow DSL2 · SQL · Java · JavaScript/Node.js · C/C++ · ARM Assembly |
| **Bioinformatics** | Flye · Minimap2 · Samtools · BUSCO · QUAST · BLAST · MultiQC |
| **Pipelines & Infra** | Nextflow · SLURM · Singularity/Apptainer · Docker · Celery · Redis · nginx · systemd |
| **Backend** | FastAPI · Django REST · SQLAlchemy · pandas · numpy · OAuth2/JWT |
| **Data** | PostgreSQL · MySQL · pandas · Parquet/FASTA/VCF/BAM wrangling |
| **Quality** | pytest · pylint · flake8 · Git/GitHub/GitLab |

---

## Experience

| | | |
|---|---|---|
| **Junior Developer** | Chert System Solutions, Lagos *(remote)* | Jun–Aug 2025 |
| **Software Developer Intern** | Schulltech, MD, US *(remote)* | May–Aug 2024 |
| **Software Developer Intern** | Bluechip Technologies, Lagos | Jun–Aug 2023 |

---

## What I care about

- **Reproducibility is a deliverable.** A pipeline that runs on your laptop and nowhere else isn't finished.
- **Negative results ship too.** Disproving your own edge is worth more than a result you didn't stress-test.
- **Preview before you mutate.** Anything touching a live system or a shared cluster shows the diff first.
- **Calibration over accuracy.** A model that says 62% and means it beats one that says 85% and doesn't.

<p align="center">
  <sub>Open to bioinformatics data engineering roles · <a href="mailto:ojulari1@gmail.com">ojulari1@gmail.com</a></sub>
</p>

<!--
BEFORE PUSHING — fill in:
  1. linkedin.com/in/YOUR-HANDLE  (line 16)
  2. FindIt-V3 and AMS have no public repo links. Either push them public and
     link the headings, or leave as-is (they still read well unlinked).
-->
