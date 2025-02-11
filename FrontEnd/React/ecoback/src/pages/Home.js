import React from 'react';
import ImageSlider from "../components/Main_Page/Slider"; 
import GaugeBar from "../components/Main_Page/GaugeBar_whole"; //오늘 절약한 컵 개수에 따라 거북이 위치 변화
import Point_Mark from "../components/Main_Page/Point_Mark"; 
import '../css/Home.css';
import { Link } from 'react-router-dom';
import TitleBanner from "../components/TitleBanner.js";
let screenWidth = window.innerWidth;
if (screenWidth > 420) {
  screenWidth = 420;
}
const fontSize = `${(screenWidth)/28}px`;
const Home = () => {
  return (
    <div className="full_container">
      <TitleBanner />
      {/*banner*/}
      <ImageSlider/>
      {/*user(사용자)의 point 표시*/}
      <Point_Mark />

      {/*이동 버튼 부분*/}

      <div id="boxline" className="normal" style={{ fontSize: `${fontSize}`}}>
      <Link to="/receiptfilming">
        <div className="box">
            <img
              src={require('../image/receipticon.png')}
              alt="receipt"
              style={{ width: '28%', height: 'auto' }}
            />

          <div >영수증 촬영</div>
        </div>
      </Link>
      <Link to="/store">
        <div className="box">
          <img
            src={require('../image/storeicon.png')}
            alt="store"
            style={{ width: '23%', height: 'auto' }}
          />
          <div>포인트 상점</div>
        </div>
      </Link>
      </div>
      <hr />
      {/*게이지바 부분 컴포넌트로 변경 */}
      <GaugeBar />
    </div>
  );
};

export default Home;
