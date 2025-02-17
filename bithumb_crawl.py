from bs4 import BeautifulSoup
import time
import cloudscraper
import time
from datetime import datetime
import re
import requests

test_html = """
<!DOCTYPE html>
<html lang="ko">

<head>
	<meta charSet="utf-8" />
	<meta name="viewport" content="width=1200" />
	<meta name="description" content="쉽고 안전한 거래는 빗썸, 비트코인, 이더리움, 리플 등 알트코인 거래, 자동매매, 스테이킹, 예치 등 다양한 서비스 제공" />
	<meta property="og:locale" content="ko_KR" />
	<meta property="og:type" content="website" />
	<meta property="og:site_name" content="No.1 가상자산 플랫폼, 빗썸" />
	<meta property="og:description" content="쉽고 안전한 거래는 빗썸, 비트코인, 이더리움, 리플 등 알트코인 거래, 자동매매, 스테이킹, 예치 등 다양한 서비스 제공" />
	<meta property="og:image" content="https://content.bithumb.com/resources/img/comm/seo/20200701_og_bithumb.png?v=bithumb2.0" />
	<meta name="twitter:card" content="summary" />
	<meta name="twitter:description" content="쉽고 안전한 거래는 빗썸, 비트코인, 이더리움, 리플 등 알트코인 거래, 자동매매, 스테이킹, 예치 등 다양한 서비스 제공" />
	<meta name="twitter:image" content="https://content.bithumb.com/resources/img/comm/seo/20200701_og_bithumb.png?v=bithumb2.0" />
	<title>공지사항 - No.1 가상자산 플랫폼, 빗썸</title>
	<meta property="og:title" content="공지사항 - No.1 가상자산 플랫폼, 빗썸" />
	<meta name="twitter:title" content="공지사항 - No.1 가상자산 플랫폼, 빗썸" />
	<meta property="og:url" content="http://feed.bithumb.com/notice" />
	<meta name="next-head-count" content="15" />
	<meta charSet="utf-8" />
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta http-equiv="X-UA-Compatible" content="IE=edge" />
	<meta http-equiv="Pragma" content="no-cache" />
	<meta http-equiv="Expires" content="0" />
	<meta http-equiv="Cache-Control" content="no-cache" />
	<link rel="icon" href="/favicon.ico" sizes="any" />
	<meta http-equiv="Content-Security-Policy" content="default-src &#x27;none&#x27;; script-src &#x27;self&#x27; &#x27;unsafe-inline&#x27; &#x27;unsafe-eval&#x27; data: blob: *.bithumb.com *.daumcdn.net *.googletagmanager.com *.appsflyer.com *.go-mpulse.net *.beusable.net *.google-analytics.com *.youtube.com *.doubleclick.net *.google.com *.gstatic.com *.facebook.net *.facebook.com *.googleapis.com *.jquery.com 127.0.0.1:55920 127.0.0.1:55921 127.0.0.1:55922 unpkg.com *.unpkg.com *.tradingview.com; style-src &#x27;self&#x27; &#x27;unsafe-inline&#x27; *.bithumb.com *.youtube.com *.github.io *.googleapis.com *.gstatic.com; img-src &#x27;self&#x27; data: content: mediastream: blob: filesystem: *.bithumb.com *.google-analytics.com *.google.com *.google.co.kr *.youtube.com *.facebook.com *.googletagmanager.com *.pstatic.net *.gstatic.com steemitimages.com *.medium.com *.googleusercontent.com; connect-src &#x27;self&#x27; blob: ws: wss: http: https: *.bithumb.com *.doubleclick.net *.sentry.io *.youtube.com *.googleapis.com *.googlevideo.com *.google.com *.google-analytics.com *.akstat.io *.go-mpulse.net ws: wss: http: https: *.walletconnect.org klipwallet.com dosivault.page.link *.astxsvc.com *.telegram.org; font-src &#x27;self&#x27; data: *.bithumb.com *.gstatic.com *.jsdelivr.net *.googleapis.com *.gstatic.com; frame-src &#x27;self&#x27; data: *.bithumb.com *.google.com *.facebook.com *.youtube.com *.daum.net *.tradingview.com *.googletagmanager.com; media-src &#x27;self&#x27; data: blob: *;"
	/>
	<link data-next-font="" rel="preconnect" href="/" crossorigin="anonymous" />
	<script id="mobile-redirect" data-nscript="beforeInteractive">
		var userAgent = window.navigator.userAgent || window.navigator.vendor;
		var isMobile = /(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(userAgent) || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw-(n|u)|c55\/|capi|ccwa|cdm-|cell|chtm|cldc|cmd-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc-s|devi|dica|dmob|do(c|p)o|ds(12|-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(-|_)|g1 u|g560|gene|gf-5|g-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd-(m|p|t)|hei-|hi(pt|ta)|hp( i|ip)|hs-c|ht(c(-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i-(20|go|ma)|i230|iac( |-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|-[a-w])|libw|lynx|m1-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|-([1-8]|c))|phil|pire|pl(ay|uc)|pn-2|po(ck|rt|se)|prox|psio|pt-g|qa-a|qc(07|12|21|32|60|-[2-7]|i-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h-|oo|p-)|sdk\/|se(c(-|0|1)|47|mc|nd|ri)|sgh-|shar|sie(-|m)|sk-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h-|v-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl-|tdg-|tel(i|m)|tim-|t-mo|to(pl|sh)|ts(70|m-|m3|m5)|tx-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas-|your|zeto|zte-/i.test(userAgent.substr(0, 4));
		var pathname = window.location.pathname;

		if (isMobile) {
			window.location.replace('http://m-feed.bithumb.com' + pathname);
		}
	</script>
	<script id="theme-check" data-nscript="beforeInteractive">
		var isDarkMode = document.cookie.indexOf('custom_cookie_theme=Y') > -1;
		document.querySelector('html').setAttribute('data-theme', isDarkMode ? 'dark' : '');
	</script>
	<link rel="preload" href="/_next/static/css/6983b6c755be5593.css" as="style" />
	<link rel="stylesheet" href="/_next/static/css/6983b6c755be5593.css" data-n-g="" />
	<link rel="preload" href="/_next/static/css/92ac8b426014fa36.css" as="style" />
	<link rel="stylesheet" href="/_next/static/css/92ac8b426014fa36.css" data-n-p="" />
	<noscript data-n-css=""></noscript>
	<script defer="" nomodule="" src="/_next/static/chunks/polyfills-78c92fac7aa8fdd8.js"></script>
	<script src="/_next/static/chunks/webpack-3a55bb9bf9054fd5.js" defer=""></script>
	<script src="/_next/static/chunks/framework-dd7574e855a2ca1a.js" defer=""></script>
	<script src="/_next/static/chunks/main-ec5f789f9a35a3d5.js" defer=""></script>
	<script src="/_next/static/chunks/pages/_app-78e229d8ff69a90f.js" defer=""></script>
	<script src="/_next/static/chunks/364-9a101f5a2e9224e5.js" defer=""></script>
	<script src="/_next/static/chunks/326-76d8ff93b4be2074.js" defer=""></script>
	<script src="/_next/static/chunks/750-68101693dd518bbd.js" defer=""></script>
	<script src="/_next/static/chunks/pages/notice-64c32c84cb5e7e27.js" defer=""></script>
	<script src="/_next/static/mNmOTUVxgrAMH2G4Dp_hu/_buildManifest.js" defer=""></script>
	<script src="/_next/static/mNmOTUVxgrAMH2G4Dp_hu/_ssgManifest.js" defer=""></script>
</head>

<body>
	<div id="__next">
		<header class="Header_new-header__JIWvE">
			<nav class="Header_nav-inner__rT5S1">
				<div class="Header_nav-inner__left__pcNEe">
					<h1 class="logo"><a href="https://www.bithumb.com/react" class="Header_home__iAmDJ"><span class="blind">Bithumb</span></a></h1>
					<div class="Header_nav-list__TW5kb">
						<ul class="Header_menu-list__rAHu8">
							<li class="Header_menu-list-wrap__e4HmF"><a href="https://www.bithumb.com/react/trade/order/BTC-KRW" class="Header_menu-list-wrap__title__uvXSf">거래소</a></li>
							<li class="Header_menu-list-wrap__e4HmF"><a href="https://www.bithumb.com/react/assets/my" class="Header_menu-list-wrap__title__uvXSf">자산</a></li>
							<li class="Header_menu-list-wrap__e4HmF"><a href="https://www.bithumb.com/react/inout/deposit/KRW" class="Header_menu-list-wrap__title__uvXSf">입출금</a></li>
							<li class="Header_menu-list-wrap__e4HmF"><a href="https://www.bithumb.com/react/insight" class="Header_menu-list-wrap__title__uvXSf">시장동향</a></li>
							<li class="Header_menu-list-wrap__e4HmF"><a href="https://www.bithumb.com/react/membership" class="Header_menu-list-wrap__title__uvXSf Header_new-dot___l3vI">혜택·서비스</a></li>
							<li class="Header_menu-list-wrap__e4HmF"><a href="#" class="Header_menu-list-wrap__title__uvXSf">고객지원</a></li>
						</ul>
					</div>
				</div>
				<div class="Header_nav-inner__right__sq_0v">
					<button type="button" class="Header_all-menu__button__rwAvX"><span class="blind">전체 메뉴 펼침 버튼</span></button>
				</div>
			</nav>
		</header>
		<div class="content">
			<div class="SideNaviContent_side-navi-content__Ty2Yr">
				<nav class="SideNavi_notice-snb__pCQDA">
					<ul>
						<li><a class="SideNavi_notice-snb__link__xOHUh" aria-current="page" href="/notice">공지사항</a></li>
						<li><a class="SideNavi_notice-snb__link__xOHUh" aria-current="false" href="/press">보도자료</a></li>
						<li><a class="SideNavi_notice-snb__link__xOHUh" aria-current="false" href="/trend">가상자산 트렌드</a></li>
						<li><a class="SideNavi_notice-snb__link__xOHUh" aria-current="false" href="/manual">가상자산설명서</a></li>
						<li><a class="SideNavi_notice-snb__link__xOHUh" aria-current="false" href="/report">주요내용설명서<br/>(국문백서)</a></li>
					</ul>
				</nav>
				<div class="SideNaviContent_side-navi-content__box__xKENQ">
					<div class="ContentTop_notice__top__8HGoH">
						<h2 class="ContentTop_notice__title__sD9AE">공지사항</h2>
						<form>
							<div class="notice-search">
								<div class="ContentSearch_notice-search__search__54nxk">
									<div style="width:240px">
										<div class="InputBox_input-box__input-box__Q9prd input-box__input-box--reset">
											<input type="text" class="InputBox_input-box__input__YWtTb" autoCapitalize="off" placeholder="검색어를 입력하세요." maxLength="20" value="" />
											<button type="button" class="InputBox_input-box__btn-reset__sVzgg"><span class="blind">input 글자 삭제</span></button>
										</div>
									</div>
									<button type="submit" class="button Button_button-default__lofwJ button--primary ContentSearch_notice-search__button__SOFEo"><span class="Button_button__text__Y9TfD">검색</span></button>
								</div>
							</div>
						</form>
						<div class="ContentCategory_notice-category__y6fvQ">
							<div class="ContentCategory_notice-category__box__Q__sZ ContentCategory_notice-category__box--right__Qp_cK">
								<ul class="ContentCategory_notice-category-list__1aHzK">
									<li>
										<button type="button" class="ContentCategory_notice-category__menu-button__b_PO_ ContentCategory_notice-category__menu-button--active__RUxwU">전체</button>
									</li>
									<li>
										<button type="button" class="ContentCategory_notice-category__menu-button__b_PO_">거래유의</button>
									</li>
									<li>
										<button type="button" class="ContentCategory_notice-category__menu-button__b_PO_">거래지원종료</button>
									</li>
									<li>
										<button type="button" class="ContentCategory_notice-category__menu-button__b_PO_">마켓 추가</button>
									</li>
									<li>
										<button type="button" class="ContentCategory_notice-category__menu-button__b_PO_">신규서비스</button>
									</li>
									<li>
										<button type="button" class="ContentCategory_notice-category__menu-button__b_PO_">안내</button>
									</li>
									<li>
										<button type="button" class="ContentCategory_notice-category__menu-button__b_PO_">업데이트</button>
									</li>
									<li>
										<button type="button" class="ContentCategory_notice-category__menu-button__b_PO_">이벤트</button>
									</li>
									<li>
										<button type="button" class="ContentCategory_notice-category__menu-button__b_PO_">입출금</button>
									</li>
									<li>
										<button type="button" class="ContentCategory_notice-category__menu-button__b_PO_">점검</button>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<ul class="NoticeContentList_notice-list__i337r">
						<li><a href="/notice/1647001" class="NoticeContentList_notice-list__link__LAkAV NoticeContentList_notice-list__link--fixed__KF7qd"><span class="NoticeContentList_notice-list__category__cBqMf">안내</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">100만원 미만 가상자산 출금 방식 변경 안내</span><span class="NoticeContentList_notice-list__badge__wg99_ NoticeContentList_notice-list__badge--new__I0u__"><span class="blind">NEW</span></span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2025.02.14</span></a></li>
						<li><a href="/notice/1646894" class="NoticeContentList_notice-list__link__LAkAV NoticeContentList_notice-list__link--fixed__KF7qd"><span class="NoticeContentList_notice-list__category__cBqMf">안내</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">창립 11주년 캠페인 감사 인사 및 일정 안내</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2025.02.06</span></a></li>
						<li><a href="/notice/1645753" class="NoticeContentList_notice-list__link__LAkAV NoticeContentList_notice-list__link--fixed__KF7qd"><span class="NoticeContentList_notice-list__category__cBqMf">이벤트</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">KB국민은행 계좌 사전등록 이벤트 - 총 1OO억을 드립니다!</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2025.01.23</span></a></li>
						<li><a href="/notice/1645041" class="NoticeContentList_notice-list__link__LAkAV NoticeContentList_notice-list__link--fixed__KF7qd"><span class="NoticeContentList_notice-list__category__cBqMf">안내</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">원화 입출금 은행 전환에 따른 사전등록 오픈 안내 - KB국민은행</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2025.01.20</span></a></li>
						<li><a href="/notice/1645391" class="NoticeContentList_notice-list__link__LAkAV NoticeContentList_notice-list__link--fixed__KF7qd"><span class="NoticeContentList_notice-list__category__cBqMf">안내</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">창립 11주년 기념 - 두번째, 거래소 이동 지원금 대상 확대 및 혜택 업그레이드! 3억원 상당의 투자지원금을 드립니다!</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2025.01.09</span></a></li>
						<li><a href="/notice/1645368" class="NoticeContentList_notice-list__link__LAkAV NoticeContentList_notice-list__link--fixed__KF7qd"><span class="NoticeContentList_notice-list__category__cBqMf">안내</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">창립 11주년 기념 - 열한번째, 과거와 완벽하게 달라진 빗썸 서비스를 만나보세요.</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2024.12.31</span></a></li>
						<li><a href="/notice/1645297" class="NoticeContentList_notice-list__link__LAkAV NoticeContentList_notice-list__link--fixed__KF7qd"><span class="NoticeContentList_notice-list__category__cBqMf">이벤트</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">창립 11주년 기념 - 일곱번째, 빗썸으로 입금하면 최대 100만원 상당의 혜택을 드립니다!</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2024.12.06</span></a></li>
						<li><a href="/notice/1645205" class="NoticeContentList_notice-list__link__LAkAV NoticeContentList_notice-list__link--fixed__KF7qd"><span class="NoticeContentList_notice-list__category__cBqMf">안내</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">안쓰면 손해! 빗썸 고객님이라면 꼭 써야하는 필수 서비스를 소개합니다!</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2024.11.13</span></a></li>
						<li><a href="/notice/1645178" class="NoticeContentList_notice-list__link__LAkAV NoticeContentList_notice-list__link--fixed__KF7qd"><span class="NoticeContentList_notice-list__category__cBqMf">신규서비스</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">창립 11주년 기념 - 두번째, 거래소 이동 지원금 프로그램 오픈! 지금 빗썸으로 오시면 최소 100만원 ~ 최대 20억원 상당을 지원해 드립니다!</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2024.10.30</span></a></li>
						<li><a href="/notice/1644003" class="NoticeContentList_notice-list__link__LAkAV NoticeContentList_notice-list__link--fixed__KF7qd"><span class="NoticeContentList_notice-list__category__cBqMf">안내</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">빗썸 사칭 주의 안내</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2024.10.02</span></a></li>
						<li><a href="/notice/1644964" class="NoticeContentList_notice-list__link__LAkAV NoticeContentList_notice-list__link--fixed__KF7qd"><span class="NoticeContentList_notice-list__category__cBqMf">안내</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">가상자산이용자보호법 준수 첫번째, 원화 예치금이용료 지급 (연 2.2%)</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2024.07.19</span></a></li>
						<li><a href="/notice/1644950" class="NoticeContentList_notice-list__link__LAkAV NoticeContentList_notice-list__link--fixed__KF7qd"><span class="NoticeContentList_notice-list__category__cBqMf">안내</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">｢가상자산 이용자 보호 등에 관한 법률｣ 시행에 따른 거래시 유의사항 안내</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2024.07.18</span></a></li>
						<li><a href="/notice/1640868" class="NoticeContentList_notice-list__link__LAkAV NoticeContentList_notice-list__link--fixed__KF7qd"><span class="NoticeContentList_notice-list__category__cBqMf">거래유의/거래지원종료</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">거래유의종목 및 거래지원 종료 일정 안내</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2024.07.05</span></a></li>
						<li><a href="/notice/1644568" class="NoticeContentList_notice-list__link__LAkAV NoticeContentList_notice-list__link--fixed__KF7qd"><span class="NoticeContentList_notice-list__category__cBqMf">안내</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">특별 메이커 리워드 적용 등급 확대 및 &#x27;블랙 프리미엄&#x27; 그랜드 오픈</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2024.02.27</span></a></li>
						<li><a href="/notice/1643910" class="NoticeContentList_notice-list__link__LAkAV NoticeContentList_notice-list__link--fixed__KF7qd"><span class="NoticeContentList_notice-list__category__cBqMf">안내</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">전기통신금융사기 주의 안내(검찰청 사칭)</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2023.06.23</span></a></li>
						<li><a href="/notice/1642918" class="NoticeContentList_notice-list__link__LAkAV NoticeContentList_notice-list__link--fixed__KF7qd"><span class="NoticeContentList_notice-list__category__cBqMf">안내</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">가상자산 거래에 관한 위험 고지</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2022.05.20</span></a></li>
						<li><a href="/notice/1646996" class="NoticeContentList_notice-list__link__LAkAV"><span class="NoticeContentList_notice-list__category__cBqMf">마켓 추가</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">테나(THE) 원화 마켓 추가</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2025.02.14</span></a></li>
						<li><a href="/notice/1646995" class="NoticeContentList_notice-list__link__LAkAV"><span class="NoticeContentList_notice-list__category__cBqMf">안내</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">스토리(IP) 거래수수료 오류 환급 안내</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2025.02.14</span></a></li>
						<li><a href="/notice/1646897" class="NoticeContentList_notice-list__link__LAkAV"><span class="NoticeContentList_notice-list__category__cBqMf">입출금</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">퀀텀(QTUM), 키 토큰(QI) 입출금 일시 중지 안내 (02/15 재개)</span><span class="NoticeContentList_notice-list__badge__wg99_ NoticeContentList_notice-list__badge--update__Bz03D"><span class="blind">Update</span></span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2025.02.14</span></a></li>
						<li><a href="/notice/1646984" class="NoticeContentList_notice-list__link__LAkAV"><span class="NoticeContentList_notice-list__category__cBqMf">이벤트</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">스토리(IP) 원화 마켓 추가 기념 에어드랍 이벤트</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2025.02.13</span></a></li>
						<li><a href="/notice/1646978" class="NoticeContentList_notice-list__link__LAkAV"><span class="NoticeContentList_notice-list__category__cBqMf">입출금</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">폴리곤 에코시스템 토큰(POL) 관련 가상자산 입출금 일시 중지 안내 (02/14 재개)</span><span class="NoticeContentList_notice-list__badge__wg99_ NoticeContentList_notice-list__badge--update__Bz03D"><span class="blind">Update</span></span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2025.02.13</span></a></li>
						<li><a href="/notice/1646927" class="NoticeContentList_notice-list__link__LAkAV"><span class="NoticeContentList_notice-list__category__cBqMf">신규서비스</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">종목 추천 서비스-두번째, 급등알림 서비스 오픈! 상승 확률이 높은 시점에 급등알림을 보내드립니다.</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2025.02.12</span></a></li>
						<li><a href="/notice/1646926" class="NoticeContentList_notice-list__link__LAkAV"><span class="NoticeContentList_notice-list__category__cBqMf">입출금</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">코스모스(ATOM) 입출금 일시 중지 안내 (02/13 재개)</span><span class="NoticeContentList_notice-list__badge__wg99_ NoticeContentList_notice-list__badge--update__Bz03D"><span class="blind">Update</span></span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2025.02.12</span></a></li>
						<li><a href="/notice/1646917" class="NoticeContentList_notice-list__link__LAkAV"><span class="NoticeContentList_notice-list__category__cBqMf">안내</span><span class="NoticeContentList_notice-list__inner__aSUqu"><span class="NoticeContentList_notice-list__link-title__nlmSC">트래블룰 솔루션 CODE 연동 VASP 추가 안내</span></span><span class="NoticeContentList_notice-list__link-date__gDc6U">2025.02.12</span></a></li>
					</ul>
					<div class="Pagination_pagination__a_Ju8">
						<button type="button" class="Pagination_pagination__button-arrow-type1__8oY6t" disabled=""><span class="blind">처음 페이지</span></button>
						<button type="button" class="Pagination_pagination__button-arrow-type2__tqRIw Pagination_pagination__button-arrow-type2--prev__T6h0Y" disabled=""><span class="blind">이전 페이지</span></button>
						<button type="button" class="Pagination_pagination__button__b7Zuq Pagination_pagination__button--active__N2qk7"><span class="pagination__button-text">1</span></button>
						<button type="button" class="Pagination_pagination__button__b7Zuq"><span class="pagination__button-text">2</span></button>
						<button type="button" class="Pagination_pagination__button__b7Zuq"><span class="pagination__button-text">3</span></button>
						<button type="button" class="Pagination_pagination__button__b7Zuq"><span class="pagination__button-text">4</span></button>
						<button type="button" class="Pagination_pagination__button__b7Zuq"><span class="pagination__button-text">5</span></button>
						<button type="button" class="Pagination_pagination__button__b7Zuq"><span class="pagination__button-text">6</span></button>
						<button type="button" class="Pagination_pagination__button__b7Zuq"><span class="pagination__button-text">7</span></button>
						<button type="button" class="Pagination_pagination__button__b7Zuq"><span class="pagination__button-text">8</span></button>
						<button type="button" class="Pagination_pagination__button__b7Zuq"><span class="pagination__button-text">9</span></button>
						<button type="button" class="Pagination_pagination__button__b7Zuq"><span class="pagination__button-text">10</span></button>
						<button type="button" class="Pagination_pagination__button-arrow-type2__tqRIw Pagination_pagination__button-arrow-type2--next__unaxH"><span class="blind">다음 페이지</span></button>
						<button type="button" class="Pagination_pagination__button-arrow-type1__8oY6t Pagination_pagination__button-arrow-type1--last__3EDKW"><span class="blind">마지막 페이지</span></button>
					</div>
				</div>
			</div>
		</div>
		<footer class="Footer_footer__X1Jp0">
			<div class="Footer_footer__inner__K8uEn">
				<p class="Footer_footer__text__Ox_Un"><span class="Footer_footer__text--gray__lE9Y8">주식회사 빗썸</span><span class="Footer_footer__bar__y6Vf6"></span><span class="Footer_footer__text--gray__lE9Y8">서울특별시 강남구 테헤란로 124, 11, 14~18층 (역삼동, 삼원타워)</span><span class="Footer_footer__bar__y6Vf6"></span>
					<span
					class="Footer_footer__text--gray__lE9Y8">대표이사 : 이재원</span><span class="Footer_footer__bar__y6Vf6"></span><span class="Footer_footer__text--gray__lE9Y8">사업자등록번호 : 220-88-71844</span></p>
					<p class="Footer_footer__text__Ox_Un"><span class="Footer_footer__text--gray__lE9Y8">투자자보호센터 : </span> 서울 서초구 강남대로 343, 신덕빌딩 1층<span class="Footer_footer__bar__y6Vf6"></span>운영시간 : 평일 9:00 ~ 18:00 (주말, 공휴일 휴무)<span class="Footer_footer__bar__y6Vf6"></span><a href="https://safebithumb.com"
						class="Footer_footer__link__mE9bw" target="_blank" rel="noopener noreferrer">투자자보호센터 바로가기</a></p>
						<p class="Footer_footer__text__Ox_Un"><span class="Footer_footer__text--gray__lE9Y8">전화상담 : </span> 1661-5566<span class="Footer_footer__bar__y6Vf6"></span>운영시간 : 365일 24시간 운영</p>
						<p class="Footer_footer__text__Ox_Un"><span class="Footer_footer__text--gray__lE9Y8">카카오톡 상담 : </span> <a href="https://pf.kakao.com/_hEurd" class="Footer_footer__link__mE9bw" target="_blank" rel="noopener noreferrer">@빗썸 (챗봇 상담)</a> (24시간 운영)</p><address class="Footer_footer__copyright__lU8vS">Copyright © Bithumb. All rights reserved.</address></div>
					</footer>
					<div class="Toast_toast___QUfd"></div>
					<noscript>
						<iframe title="Google Tag Manager (noscript)" src="https://www.googletagmanager.com/ns.html?id=GTM-TZKP2QTB" height="0" width="0" style="display:none;visibility:hidden"></iframe>
					</noscript>
				</div>
				<script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"status":"ok","noticeList":[{"id":1647001,"boardType":"1","categoryName1":"안내","categoryName2":null,"title":"100만원 미만 가상자산 출금 방식 변경 안내","topFixYn":"Y","publicationDateTime":"2025-02-14 18:00:10","modifyDateTime":"2025-02-17
					12:03:53","modifyDateTimeExposureYn":"N"},{"id":1646894,"boardType":"1","categoryName1":"안내","categoryName2":null,"title":"창립 11주년 캠페인 감사 인사 및 일정 안내","topFixYn":"Y","publicationDateTime":"2025-02-06 18:00:28","modifyDateTime":"2025-02-06 18:43:51","modifyDateTimeExposureYn":"N"},{"id":1645753,"boardType":"1","categoryName1":"이벤트","categoryName2":null,"title":"KB국민은행
					계좌 사전등록 이벤트 - 총 1OO억을 드립니다!","topFixYn":"Y","publicationDateTime":"2025-01-23 17:11:35","modifyDateTime":"2025-02-06 15:14:17","modifyDateTimeExposureYn":"N"},{"id":1645041,"boardType":"1","categoryName1":"안내","categoryName2":null,"title":"원화
					입출금 은행 전환에 따른 사전등록 오픈 안내 - KB국민은행","topFixYn":"Y","publicationDateTime":"2025-01-20 09:01:13","modifyDateTime":"2025-02-13 14:11:38","modifyDateTimeExposureYn":"N"},{"id":1645391,"boardType":"1","categoryName1":"안내","categoryName2":null,"title":"창립
					11주년 기념 - 두번째, 거래소 이동 지원금 대상 확대 및 혜택 업그레이드! 3억원 상당의 투자지원금을 드립니다!","topFixYn":"Y","publicationDateTime":"2025-01-09 18:55:48","modifyDateTime":"2025-01-31 18:24:14","modifyDateTimeExposureYn":"N"},{"id":1645368,"boardType":"1","categoryName1":"안내","categoryName2":null,"title":"창립
					11주년 기념 - 열한번째, 과거와 완벽하게 달라진 빗썸 서비스를 만나보세요.","topFixYn":"Y","publicationDateTime":"2024-12-31 18:41:58","modifyDateTime":"2024-12-31 18:41:59","modifyDateTimeExposureYn":"N"},{"id":1645297,"boardType":"1","categoryName1":"이벤트","categoryName2":null,"title":"창립
					11주년 기념 - 일곱번째, 빗썸으로 입금하면 최대 100만원 상당의 혜택을 드립니다!","topFixYn":"Y","publicationDateTime":"2024-12-06 19:57:31","modifyDateTime":"2025-02-10 11:00:06","modifyDateTimeExposureYn":"N"},{"id":1645205,"boardType":"1","categoryName1":"안내","categoryName2":null,"title":"안쓰면
					손해! 빗썸 고객님이라면 꼭 써야하는 필수 서비스를 소개합니다!","topFixYn":"Y","publicationDateTime":"2024-11-13 10:59:56","modifyDateTime":"2024-11-15 21:58:52","modifyDateTimeExposureYn":"N"},{"id":1645178,"boardType":"1","categoryName1":"신규서비스","categoryName2":null,"title":"창립
					11주년 기념 - 두번째, 거래소 이동 지원금 프로그램 오픈! 지금 빗썸으로 오시면 최소 100만원 ~ 최대 20억원 상당을 지원해 드립니다!","topFixYn":"Y","publicationDateTime":"2024-10-30 19:46:00","modifyDateTime":"2025-02-10 08:57:27","modifyDateTimeExposureYn":"N"},{"id":1644003,"boardType":"1","categoryName1":"안내","categoryName2":null,"title":"빗썸
					사칭 주의 안내","topFixYn":"Y","publicationDateTime":"2024-10-02 19:27:01","modifyDateTime":"2025-01-25 16:13:04","modifyDateTimeExposureYn":"Y"},{"id":1644964,"boardType":"1","categoryName1":"안내","categoryName2":null,"title":"가상자산이용자보호법 준수 첫번째, 원화
					예치금이용료 지급 (연 2.2%)","topFixYn":"Y","publicationDateTime":"2024-07-19 23:20:39","modifyDateTime":"2024-07-25 19:00:04","modifyDateTimeExposureYn":"N"},{"id":1644950,"boardType":"1","categoryName1":"안내","categoryName2":null,"title":"｢가상자산 이용자 보호
					등에 관한 법률｣ 시행에 따른 거래시 유의사항 안내","topFixYn":"Y","publicationDateTime":"2024-07-18 15:30:34","modifyDateTime":"2024-10-28 17:00:05","modifyDateTimeExposureYn":"N"},{"id":1640868,"boardType":"1","categoryName1":"거래유의","categoryName2":"거래지원종료","title":"거래유의종목
					및 거래지원 종료 일정 안내","topFixYn":"Y","publicationDateTime":"2024-07-05 10:00:00","modifyDateTime":"2025-02-07 15:05:18","modifyDateTimeExposureYn":"N"},{"id":1644568,"boardType":"1","categoryName1":"안내","categoryName2":null,"title":"특별 메이커 리워드 적용 등급
					확대 및 '블랙 프리미엄' 그랜드 오픈","topFixYn":"Y","publicationDateTime":"2024-02-27 12:00:00","modifyDateTime":"2024-12-10 14:53:39","modifyDateTimeExposureYn":"N"},{"id":1643910,"boardType":"1","categoryName1":"안내","categoryName2":null,"title":"전기통신금융사기
					주의 안내(검찰청 사칭)","topFixYn":"Y","publicationDateTime":"2023-06-23 09:52:10","modifyDateTime":"2023-06-23 09:52:10","modifyDateTimeExposureYn":"N"},{"id":1642918,"boardType":"1","categoryName1":"안내","categoryName2":null,"title":"가상자산 거래에 관한 위험 고지","topFixYn":"Y","publicationDateTime":"2022-05-20
					18:00:01","modifyDateTime":"2022-05-20 18:00:01","modifyDateTimeExposureYn":"N"},{"id":1647005,"boardType":"1","categoryName1":"업데이트","categoryName2":null,"title":"모카버스(MOCA) 가상자산 명칭 변경 안내","topFixYn":"N","publicationDateTime":"2025-02-17 12:00:00","modifyDateTime":"2025-02-17
					11:38:16","modifyDateTimeExposureYn":"N"},{"id":1647004,"boardType":"1","categoryName1":"안내","categoryName2":null,"title":"기존 비체인(VET) 보유 회원 대상 비토르 토큰(VTHO) 에어드랍 지원 안내","topFixYn":"N","publicationDateTime":"2025-02-17 11:00:00","modifyDateTime":"2025-02-17
					11:03:44","modifyDateTimeExposureYn":"N"},{"id":1647003,"boardType":"1","categoryName1":"점검","categoryName2":null,"title":"빗썸 포인트샵 서비스 점검 안내 (종료)","topFixYn":"N","publicationDateTime":"2025-02-15 08:02:10","modifyDateTime":"2025-02-15 10:32:22","modifyDateTimeExposureYn":"N"},{"id":1647002,"boardType":"1","categoryName1":"안내","categoryName2":null,"title":"포인트샵
					서비스 지연 안내 (정상화)","topFixYn":"N","publicationDateTime":"2025-02-14 19:20:00","modifyDateTime":"2025-02-14 20:58:05","modifyDateTimeExposureYn":"Y"},{"id":1646977,"boardType":"1","categoryName1":"입출금","categoryName2":null,"title":"인젝티브(INJ) 입출금
					일시 중지 안내","topFixYn":"N","publicationDateTime":"2025-02-14 15:00:00","modifyDateTime":"2025-02-13 10:10:34","modifyDateTimeExposureYn":"N"},{"id":1646997,"boardType":"1","categoryName1":"안내","categoryName2":null,"title":"KB국민은행 시스템 점검 작업으로 인한
					사전등록 서비스 일시 중단 안내","topFixYn":"N","publicationDateTime":"2025-02-14 13:54:50","modifyDateTime":"2025-02-14 13:54:51","modifyDateTimeExposureYn":"N"},{"id":1646996,"boardType":"1","categoryName1":"마켓 추가","categoryName2":null,"title":"테나(THE) 원화
					마켓 추가","topFixYn":"N","publicationDateTime":"2025-02-14 11:14:27","modifyDateTime":"2025-02-14 13:30:24","modifyDateTimeExposureYn":"N"},{"id":1646995,"boardType":"1","categoryName1":"안내","categoryName2":null,"title":"스토리(IP) 거래수수료 오류 환급 안내","topFixYn":"N","publicationDateTime":"2025-02-14
					11:00:31","modifyDateTime":"2025-02-14 11:00:31","modifyDateTimeExposureYn":"N"},{"id":1646897,"boardType":"1","categoryName1":"입출금","categoryName2":null,"title":"퀀텀(QTUM), 키 토큰(QI) 입출금 일시 중지 안내 (02/15 재개)","topFixYn":"N","publicationDateTime":"2025-02-14
					11:00:00","modifyDateTime":"2025-02-15 17:45:22","modifyDateTimeExposureYn":"Y"},{"id":1646984,"boardType":"1","categoryName1":"이벤트","categoryName2":null,"title":"스토리(IP) 원화 마켓 추가 기념 에어드랍 이벤트","topFixYn":"N","publicationDateTime":"2025-02-13 17:26:08","modifyDateTime":"2025-02-13
					17:41:01","modifyDateTimeExposureYn":"N"},{"id":1646978,"boardType":"1","categoryName1":"입출금","categoryName2":null,"title":"폴리곤 에코시스템 토큰(POL) 관련 가상자산 입출금 일시 중지 안내 (02/14 재개)","topFixYn":"N","publicationDateTime":"2025-02-13 12:30:00","modifyDateTime":"2025-02-14
					12:19:14","modifyDateTimeExposureYn":"Y"},{"id":1646927,"boardType":"1","categoryName1":"신규서비스","categoryName2":null,"title":"종목 추천 서비스-두번째, 급등알림 서비스 오픈! 상승 확률이 높은 시점에 급등알림을 보내드립니다.","topFixYn":"N","publicationDateTime":"2025-02-12 17:30:58","modifyDateTime":"2025-02-12
					17:45:59","modifyDateTimeExposureYn":"N"},{"id":1646926,"boardType":"1","categoryName1":"입출금","categoryName2":null,"title":"코스모스(ATOM) 입출금 일시 중지 안내 (02/13 재개)","topFixYn":"N","publicationDateTime":"2025-02-12 15:00:00","modifyDateTime":"2025-02-13
					11:18:32","modifyDateTimeExposureYn":"Y"},{"id":1646917,"boardType":"1","categoryName1":"안내","categoryName2":null,"title":"트래블룰 솔루션 CODE 연동 VASP 추가 안내","topFixYn":"N","publicationDateTime":"2025-02-12 10:00:00","modifyDateTime":"2025-02-11 18:47:58","modifyDateTimeExposureYn":"N"}],"totalCount":4246,"categories":[{"id":5,"name":"거래유의"},{"id":6,"name":"거래지원종료"},{"id":9,"name":"마켓
				추가"},{"id":2,"name":"신규서비스"},{"id":1,"name":"안내"},{"id":4,"name":"업데이트"},{"id":8,"name":"이벤트"},{"id":7,"name":"입출금"},{"id":3,"name":"점검"}]},"__N_SSP":true},"page":"/notice","query":{},"buildId":"mNmOTUVxgrAMH2G4Dp_hu","isFallback":false,"gssp":true,"scriptLoader":[]}</script>
			</body>

			</html>
"""

notify_group_token = "JyBbcigUcucMOgPud1qwmyIkDd5orgtN0SsZkm9Kdvd"

def send_message_to_notify(message):
    headers = {"Authorization": f"Bearer {notify_group_token}"}
    data = {"message": message}
    requests.post("https://notify-api.line.me/api/notify", headers=headers, data=data)


def parse(html_content, key_word):
    past_time = time.time()
    

    # Find the first item with class 'NoticeContentList_notice-list__link__LAkAV'
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <a> tags with the class containing "NoticeContentList_notice-list__link__LAkAV"
    all_items = soup.find_all('a', class_='NoticeContentList_notice-list__link__LAkAV')

    # Now filter them by checking the class exactly matches the one you're looking for
    # Iterate through the found items and return the first one with the correct class
    first_item = None
    for item in all_items:
        if len(item.get('class', [])) == 1:
            first_item = item
            break

    previos_coin = ""
    if first_item:
        # Check if the category is "마켓 추가"
        category = first_item.find('span', class_='NoticeContentList_notice-list__category__cBqMf').text
        if  key_word in category:
            # Extract the title
            title = first_item.find('span', class_='NoticeContentList_notice-list__link-title__nlmSC').text
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Found '마켓 추가': {title} at {current_time}")
             # Parse the market name (i.e., "THE" from "테나(THE) 원화 마켓 추가")
            market_name_match = re.search(r'\((.*?)\)', title)
            if market_name_match:
                coin_name = market_name_match.group(1)
                if coin_name != previos_coin:
                    send_message_to_notify(f"爬蟲監測bithumb 上幣: {coin_name}")
                    print(f"Coin Name: {coin_name}") 
                previos_coin = coin_name
            else:
                print("Coin Name not found.")
        # else:
        #     print("The first item is not '마켓 추가'.")
        
        # Measure time elapsed
    # time_elapse = time.time() - past_time
    # print(f"time cost: {time_elapse}")
    
upcoin_keyword = "마켓 추가"

def main():
    URL = "https://feed.bithumb.com/notice"

    # Set up headers to mimic a real browser
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
    }

    # Define the proxy list (replace with actual proxy IP & port)
    # Define the proxy (replace with a real proxy IP & port)
    proxies = [
        {"http": "http://23.82.137.161:80"},   # Replace with actual proxy IP & port
        {"http": "http://203.57.51.53:80"},
        {"http": "http://188.166.56.246:80"},
        {"http": "http://146.83.216.227:80"},
        {"http": "http://8.220.205.172:5060"},
        {"http": "http://159.54.187.233:8080"},
        {"http": "http://146.83.216.227:80"},
        {"http": "http://3.124.133.93:3128"},
        {"http": "http://34.135.166.24:80"},
        {"http": "http://202.61.204.51:80"}
    ]

    # Create a scraper session
    scraper = cloudscraper.create_scraper()
    interval = 0.8  # 1 second interval

    # Loop through proxies
    past_time = time.time()
    while True:
        for proxy in proxies:
            try:
                # Make the request using the current proxy
                response = scraper.get(URL, headers=headers, proxies=proxy)

                # Print the status code and latency for each request
                # print(f"Status Code: {response.status_code}")

                # Print response text if successful (optional)
                if response.status_code == 200:
                    html_content = response.text
                    parse(html_content, key_word="마켓 추가")
                else:
                    print("Request failed.")
                # print(f"Latency: {time.time() - past_time:.3f} seconds")
                past_time = time.time()
            except Exception as e:
                print(f"Error with proxy: {e}")

            # Wait for the next request (1 second) before continuing to the next proxy
            time.sleep(interval)

if __name__ == "__main__":
    print("test")
    main()
        