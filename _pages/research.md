---
layout: single
permalink: /research/
title: "Research Interests"
author_profile: true
---

<div class="research-container">

  <div class="research-section">
    <h2>Low voltage active distribution grid control</h2>
    <p>
      No grid models because <em>critical infrastructure</em>. Barely any measurements because <em>data protection and privacy</em>. Not just an electrical grid because <em>sector coupling</em>. Transformer loaded to both extremes because <em>high penetration of PV, car chargers and heat pumps</em>.<br>
      How can we optimally control and operate such active distribution grids? My collaborators have looked into this problem from the perspective of data-driven state estimation, feedback optimization, reinforcement learning, data-driven predictive control and symbolic regression. <br>
      I am interested in setting up accurate, reproducible and comprehensive experiment setups to validate these methodologies in my PHIL laboratory.
    </p>
    <div class="media-container">
      <figure>
        <img src="/images/research/project1/image1.jpg" alt="Image 1 of project 1">
        <figcaption><a href="https://arxiv.org/abs/2507.02325" target="_blank">Fig 1. PHIL setup from Graf. et al., 2025.</a></figcaption>
      </figure>
      <figure>
        <img src="/images/research/project1/image2.jpg" alt="Image 2 of project 1">
        <figcaption><a href="https://dl.acm.org/doi/pdf/10.1145/3679240.3734622" target="_blank">Fig 2. Physics inspired Symbolic Regression vs Power flow models from Eichhorn et al., 2025.</a></figcaption>
      </figure>
    </div>
  </div>

  <div class="research-section">
    <h2>Home energy management systems (HEMS) in real German grids</h2>
    <p>
      Total decarbonisation of Germany will lead to manifold increase in peak electrical demand. This requires an extremely expensive grid reinforcement. But nobody produces as many transformers as we need - right now! We need ways to slow down the need to reinforce grids. <br>
      HEMS in every household with PV, EV chargers and Heat pumps can use the sector-coupling flexibiity and reduce the peak load at the transformer. <br>
      But which <em>algorithm</em> is the best? How do we combine these with <em>smart meters and iMsys</em>? Can there be a way to combine <em>profit making with grid stabilising</em> behaviour?. <br>
      In our research project, PhyLFlex, we are partnering with the HAW Landshut, a local grid operator in Bayern and Siemens to benchmark different HEMS in the CoSES lab and demonstrate their efficacy in a field test. <br>
    </p>
    <div class="media-container">
       <figure>
        <img src="/images/research/project2/image1.jpg" alt="Image 1 of project 2">
        <figcaption><a href="https://www.haw-landshut.de/aktuelles/beitrag/ki-trifft-physik" target="_blank">Fig 1. The PhyLFlex consortium.</a></figcaption>
      </figure>
	         <figure>
        <img src="/images/research/project2/image2.jpg" alt="Image 2 of project 2">
        <figcaption><a href="https://www.linkedin.com/posts/coses-research_mit-unserem-1-hems-symposium-haben-wir-viele-activity-7245445984506306560-jghg/" target="_blank">Fig 2. Annual HEMS Symposium in TUM since 2024.</a></figcaption>
      </figure>
    </div>
  </div>
  
  <div class="research-section">
    <h2>Surrogates for energy system models</h2>
    <p>
      Can we create fast machine learning surrogates to replace the state-of-the-art but computationaly intensive Mixed-integer linear programming frameworks for energy system modeling? Turns out we can for specific applications like - upstream grid expansion planning. <br>
      We have so far looked into LSTM, Transformer and Temporal GNN approaches to predict peak and aggregated net demand at the transformer under total electrification with flexibiity through sector-coupling. Right now we are going towards a surrogate with far less input data requirements, while being suitable for most real grids in Germany.
    </p>
    <div class="media-container">
       <figure>
        <img src="/images/research/project3/image1.jpg" alt="Image for surrogates project">
        <figcaption><a href=" " target="_blank">Fig 1. Typical Tx Grid and downstrean ADG for expansion planning problems (Mohapatra et al., 2025).</a></figcaption>
      </figure>
	  <figure>
        <img src="/images/research/project3/image2.jpg" alt="Image for surrogates project">
        <figcaption><a href=" " target="_blank">Fig 2. Pre-processing GNN surrogates from Pjetri et al., 2025. </a></figcaption>
      </figure>
    </div>
  </div>
  
  <div class="research-section">
    <h2>Accurate renewable DER emulation on PHIL</h2>
    <p>
      Heat pumps, Synchronous Machines, Battery Energy Storage Systems, Combined Heat and Power Plants, Electrolysers, Fuel Cells - How do we model these on a PHIL amplifier to perform systems level validation with realistic DERs?
    </p>
    <div class="media-container">
	  <figure>
        <img src="/images/research/project4/image1.jpg" alt="Image for PHIL project">
        <figcaption><a href="https://www.sciencedirect.com/science/article/pii/S0378779624006400" target="_blank">Fig 1. PHIL Air-source heat pump from Song et al., 2024. </a></figcaption>
      </figure>
	  <figure>
        <img src="/images/research/project4/image2.jpg" alt="Image for PHIL project">
        <figcaption><a href="https://mediatum.ub.tum.de/doc/1726262/1726262.pdf" target="_blank">Fig 2. PHIL synchronous machine from Mohapatra, 2024 (PhD. Thesis). </a></figcaption>
      </figure>
    </div>
  </div>
  
  <div class="research-section">
    <h2>Enabling interdisciplinary research for active distribution grids</h2>
    <p>
      Electrical engineers will not save the world! We need every type of engineer, researcher, policy maker and even the common man to participate in the power system transformation journey. But how do we manage to get around the equations, simulations, solvers and tools made exclusively for an electrical engineer? <br>
      Digital twins which abstract the most important features of the underlying system? Virtual reality to compare controllers? Benchmarking platforms to test your idea without a crash course in electrical engineering? Public events to demystify concepts of 100% renewable grid operation? <br>
      I am generally interested in any and all such ideas.
    </p>
    <div class="media-container">
      <figure>
        <img src="/images/research/project5/image1.JPG" alt="Image for interdisciplinary research">
        <figcaption><a href="https://www.mep.tum.de/mep/aktuelles/news-single-view/article/einweihung-des-neuen-schuelerlabors/" target="_blank">Fig 1. The energy lab for school students in TUM. </a></figcaption>
      </figure>
	  <figure>
        <img src="/images/research/project5/image2.jpg" alt="Image for interdisciplinary research">
        <figcaption><a href="https://forschungscampus-garching.de/" target="_blank">Fig 2. CoSES exhibits for the campus open door day. </a></figcaption>
      </figure>
    </div>
  </div>  

</div>