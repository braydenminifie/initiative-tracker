import "./Button.css";

const Button = ({ children, variant = "default", onClick}) => {
    return (
    <button className={`btn btn--${variant}`} onClick={onClick}>
      {children}
    </button>
  );
};

export default Button