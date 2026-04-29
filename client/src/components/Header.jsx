import React from "react";
import HeaderButton from "./HeaderButton"
import "./Header.css"

const Header = () => {
    return <div id = "header">
        <p class = "header-text">Initiative Tracker</p>
        <HeaderButton label = "Encounters"/>
    </div>
};

export default Header