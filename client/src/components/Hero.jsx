import React from "react";
import "./Hero.css";

const Hero = ({image, title, subtitle}) => {
  return (
    <section
      className="hero"
      style={{ backgroundImage: `url(${image})` }}>

      <div className="hero-overlay">
        <h1 className="hero-title">{title}</h1>
        <p className="hero-subtitle">{subtitle}</p>
      </div>
      
    </section>
  );
};

export default Hero;