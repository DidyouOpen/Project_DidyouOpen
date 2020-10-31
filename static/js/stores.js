let mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao.maps.LatLng(36.809982, 127.111104), // 처음 나타날 지도 위치 위, 경도
        level: 3 // 지도의 확대 레벨
    };
/***********************지도 생성***************************/
let map = new kakao.maps.Map(mapContainer, mapOption);


/***********************인포윈도우 컨텐츠를 정의함***************************/
let iwRemoveable = true;        // 인포 윈도우 내 'X' 버튼 정의
let positions = [
    {
        content: '<div class="infoWindows">' +
            '<img src="img/img1.jpg" alt = "My Image" width="100px" height="100px" class="infoWindows-img">' +
            '<div class="infoWindows-sub">'+
            '<b class="infoWindows-sub-title">스타벅스 천안 불당점</b>' +
            '<span class="infoWindows-sub-description">' +
                '시애틀에 본사를 두고 있고 간단한 스낵과 무료 Wi-Fi를 제공 하는 유명 커피 체인점 입니다.' +
            '</span>' +
            '<div class="infoWindows-Button">'+
            '<input type=button style="width:50pt;height:20pt;" value="Open">' +
            '<input type=button style="width:50pt;height:20pt;" value="Close">' +
            // 아래 버튼에 예약 페이지 링크 첨부 하시면 됩니다
            '<input type="button" style="width:70pt;height:20pt;" value="예약">' +
            '</div>'+
            '</div>'+

        '</div>',
        removable: iwRemoveable,
        latlng: new kakao.maps.LatLng(36.809982, 127.111104)
    },
];

/***********************마커 및 인포윈도우 생성***************************/
for (var i = 0; i < positions.length; i ++) {
    // 마커를 생성
    var marker = new kakao.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: positions[i].latlng, // 마커의 위치
        clickable: true,
    });

    let infowindow = new kakao.maps.InfoWindow({
        content: positions[i].content, // 인포윈도우에 표시할 내용
        removable: iwRemoveable,
    });

    kakao.maps.event.addListener(marker, 'click', function() {
        // 마커 위에 인포윈도우를 표시합니다
        infowindow.open(map, marker);
    });
}