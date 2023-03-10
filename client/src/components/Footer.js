import React from 'react';
import { Link } from 'react-router-dom';

const Footer = () => {
  return (
    <footer className="bg-primary py-12">
      <div className="container mx-auto">
        <p className="text-white text-center">2023 &copy; <Link to={"https://github.com/yuvidcreator/"}>Yuvraaj</Link>. All Rights Reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;
