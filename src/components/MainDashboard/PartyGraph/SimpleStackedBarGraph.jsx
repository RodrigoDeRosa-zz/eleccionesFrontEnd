import React, { PureComponent } from 'react';
import {
    BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer,
} from 'recharts';

const data = [
    {
        name: 'Juntos por el Cambio', macri: 4000, picheto: 2400,
    },
    {
        name: 'Somos', cristina: 3000, fernandez: 1398,
    },
];

export default class SimpleStackedBarGraph extends PureComponent {

    render() {
        return (
            <div style={{ width: '100%', height: 500 }}>
                <ResponsiveContainer>
                    <BarChart
                        width={500}
                        height={300}
                        data={this.props.data}
                        margin={{
                            top: 20, right: 30, left: 20, bottom: 5,
                        }}
                    >
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="name" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        {this.props.labels.map((candidate, index) =>
                            <Bar key={index} dataKey={candidate.name} stackId="a" fill={candidate.color} />
                        )}
                    </BarChart>
                </ResponsiveContainer>
            </div>
        );
    }
}
