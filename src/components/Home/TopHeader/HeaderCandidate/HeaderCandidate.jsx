import React from 'react';
import { hot } from 'react-hot-loader';
import './HeaderCandidate.scss';

class HeaderCandidate extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            isActive: false,
        };
    }

    changeActive = () => {
        this.setState({ isActive: !this.state.isActive });
        this.props.onClick(this.props.candidate.name, this.state.isActive);
    };

    render() {
        return (
            <div className="header-candidate-wrapper" onClick={this.changeActive}>
                <img
                    alt={this.props.candidate.name}
                    className={"header-candidate-img " + (this.state.isActive ? "forth-br-color" : "forth-br-color-dark")}
                    src={this.props.candidate.image}
                />
                <span
                    className={"header-candidate-text " + (this.state.isActive ? "forth-font-color" : "fifth-font-color")}>
                    {this.props.candidate.name.split(' ')[0]}
                </span>
                <span
                    className={"header-candidate-text " + (this.state.isActive ? "forth-font-color" : "fifth-font-color")}>
                    {this.props.candidate.name.split(' ')[1]}
                </span>
            </div>
        );
    }
}

export default hot(module)(HeaderCandidate);
