# SKA RealTime Seismic

**Entropy-driven, real-time seismic regime detection and analysis with the Structured Knowledge Accumulation (SKA) framework**


## Overview

**SKA RealTime Seismic** applies the Structured Knowledge Accumulation (SKA) framework—a novel entropy-minimizing, forward-only learning algorithm—to continuous seismic data streams.
The goal: **Reveal hidden transitions, clustering, and regime changes in earthquake microstructure,** beyond what classical seismology or statistical methods can provide.

* **Real-time entropy learning:** Compute entropy and regime transitions for each seismic event, even in dense or quiescent periods.
* **Regime detection:** Discover subtle state changes and clustering in seismic signals.
* **Open-source:** Reproducible code, sample data, and tools for the seismology community.



## Features

* Live or historical seismic data analysis with SKA entropy learning
* Regime segmentation and transition visualization in earthquake sequences
* Tools for entropy trajectories, event clustering, and regime cycling analysis
* Open data format (compatible with [Obspy](https://github.com/obspy/obspy) and [FDSN](https://www.fdsn.org/))



## Quick Start

1. **Clone the repo**

   ```bash
   git clone https://github.com/quantiota/SKA-RealTime-Seismic.git
   ```
2. **Install requirements**

   ```bash
   pip install -r requirements.txt
   ```
3. **Run analysis**

   * See sample scripts in `scripts/` or notebooks in `notebooks/`
   * Compatible with standard seismic event CSVs or waveform streams


## Example Output

> *(Insert a figure or plot here showing SKA entropy trajectories or regime transitions on seismic event data)*



## Why SKA for Seismology?

* Detects information-theoretic regime changes that are invisible to standard clustering/statistics
* Quantifies entropy in both active and quiescent periods—enabling new types of microstructure analysis
* Adaptable for real-time monitoring, earthquake clustering, or anomaly detection



## Collaboration

**We welcome collaboration with open-source seismology developers, researchers, and institutions.**

* Apply SKA to your seismic networks, catalogues, or event streams
* Comparative studies: SKA vs. classical clustering, machine learning, or forecast models
* Real-time applications: Early warning, aftershock/foreshock detection, microseismicity studies

*Open an issue or contact us for joint projects!*



## Citation

If you use this work, please cite:

* Bouarfa Mahi.
  
  * **Structured Knowledge Accumulation: An Autonomous Framework for Layer-Wise Entropy Reduction in Neural Learning**
  [arXiv:2503.13942](https://arxiv.org/abs/2503.13942)

  * **Structured Knowledge Accumulation: The Principle of Entropic Least Action in Forward-Only Neural Learning**
   [arXiv:2504.13942](https://arxiv.org/abs/2503.03214)

## License

MIT License



*SKA RealTime Seismic bridges information theory and seismology, providing a new lens on earthquake microstructure and regime dynamics.*


