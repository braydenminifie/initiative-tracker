import React from "react";
import "./Header.css"

const HeaderButton = ({label, onClick}) => {
  return (<button onClick = {onClick}
            className = "header-button">
        {label}
        </button>
    );
};

export default HeaderButton;