import React, { useState, useEffect } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { Button, Row, Col, ListGroup, Image, Card } from 'react-bootstrap';
import { useDispatch, useSelector } from 'react-redux';
import Message from '../components/Message';
import { saveShippingAddress } from '../actions/cartActions';
import CheckoutSteps from '../components/CheckoutSteps';


function PlaceOrderScreen() {
    const cart = useSelector(state => state.cart)
    return (
        <Row>
            <CheckoutSteps step1 step2 step3 step4 />
            <Col md={8}>
                <ListGroup variant='flush'>
                    <ListGroup.Item>
                        <h2>Shipping</h2>
                        <p>
                            <strong>Shipping: </strong>
                            {cart.shippingAddress.address}, {cart.shippingAddress.city}
                            {'  '}
                            {cart.shippingAddress.postalCode},
                            {'  '}
                            {cart.shippingAddress.country}
                        </p>
                    </ListGroup.Item>
                </ListGroup>
            </Col>
            <Col md={4}>

            </Col>
        </Row>
    )
}

export default PlaceOrderScreen