import "./Button.css";

const Button = ({ children, variant = "default", onClick}) => {
    return (
    <button className={`btn btn--${variant}`} onClick={onClick}>
      <span className="btn-text">{children}</span>
    </button>
  );
};

export default Button