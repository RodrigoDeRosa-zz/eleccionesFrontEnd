import React from 'react';
import { connect } from "react-redux";
import { getCandidates } from "../../actions/index";
import './Home.scss';
import TopHeader from "./TopHeader/TopHeader";

const CANDIDATES = [
    {name:'Cristina Kirchner' , image:'https://pbs.twimg.com/profile_images/1112014698/foto6-3.jpg_1__400x400.jpg'},
    {name:'Mauricio Macri' , image:'https://pbs.twimg.com/profile_images/653558348273569792/joxg8DZD_400x400.png'},
    {name:'Sergio Massa' , image:'https://pbs.twimg.com/profile_images/1087745699435954177/s2avaP4Z_400x400.jpg'},
    {name:'Roberto Lavagna' , image:'https://pbs.twimg.com/profile_images/1109111637200551936/XxjhOVXq_400x400.jpg'},
    {name:'Juan Manuel Urtubey' , image:'https://pbs.twimg.com/profile_images/1111700077389721602/aQpR-fm9_400x400.jpg'},
    {name:'Jose Luis Espert' , image:'https://pbs.twimg.com/profile_images/996372022174339072/igFlqf4c_400x400.jpg'},
    {name:'Alberto Fernández' , image:'https://pbs.twimg.com/profile_images/1132570874387795968/AvHOBR0d_400x400.jpg'},
];

const mapStateToProps = state => {
    return {
        activeCandidates: state.activeCandidates,
        candidates: state.candidates,
    };
};

class HomeConnected extends React.Component {

    componentDidMount() {
        this.props.getCandidates();
    }

    render() {
        return (
            <main>
                <TopHeader candidates={CANDIDATES.sort(function() { return 0.5 - Math.random() })} />
                {this.props.activeCandidates.map(candidate => (candidate.candidate))}
            </main>
        );
    }
}


const Home = connect(mapStateToProps, {getCandidates})(HomeConnected);
export default Home;
