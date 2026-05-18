import React from "react";
import HeaderButton from "./HeaderButton"
import "./Header.css"
import { Link } from "react-router-dom";

const Header = () => {
    return <div id = "header">
        <p className = "header-text">Initiative Tracker</p>
        <Link
            to={`/encounters`}
            >
            <HeaderButton label = "Encounters"/>
        </Link>
    </div>
};

export default Header