import './receiptFilming.css'
import Webcam from "react-webcam";
import Camera from './Camera.js'
import TitleBanner from "../components/TitleBanner.js"
import BackbuttonBar from 'components/BackbuttonBar';
const WebcamComponent = () => <Webcam />;
const ReceiptFilming=()=>{
    return (
    <div className="full_container">
        <div class="filmingPage" >
            <TitleBanner />
            <hr />
            <BackbuttonBar title="영수증 촬영"/>
            <div id="camera">
                <Camera />
            </div>
        </div>
    </div>
    );};

export default ReceiptFilming;