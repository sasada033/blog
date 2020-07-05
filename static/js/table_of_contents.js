$(window).on('load', function() {
	/* -------------------------------------------------------
		記事の見出しから目次作成
	--------------------------------------------------------*/
	function makeMokuji() {
		
		var idcount = 1;
		var mokuji = '';
		var toc = '<ol class="chapter">';
		var currentlevel = 0
		var sectionTopArr = new Array();
		
		// 見出しを回してリストに格納
		$('article h2, article h3, article h4').each(function(i){
			
			// IDを保存
			this.id = 'chapter-' + idcount;
			idcount ++;
			
			// 見出しの入れ子
			var level = 0;
			if(this.nodeName.toLowerCase() == 'h2') {
				level = 1;
				toc += '<li><a href="#' + this.id + '">' + $(this).html() + '</a></li>\n';
			} else if(this.nodeName.toLowerCase() == 'h3') {
				level = 2;
			} else if(this.nodeName.toLowerCase() == 'h4') {
				level = 3;
			}
			while(currentlevel < level) {
				mokuji += '<ol class="chapter">';
				currentlevel ++;
			}
			while(currentlevel > level) {
				mokuji += '</ol>';
				currentlevel --;
			}
			
			// リストを生成
			mokuji += '<li><a href="#' + this.id + '">' + $(this).html() + '</a></li>\n';
		});
	
		while(currentlevel > 0) {
			mokuji += '</ol>';
			currentlevel --;
		}

		toc += '</ol>';
				
		// HTML出力
		strMokuji = '<h4>目次一覧</h4><div class="mokujiInner">'
						+ mokuji +
					 '<!-- /.mokujiInner --></div>';
					
		$('.mokuji').html(strMokuji);
		$('.toc-block').html(toc);
		
		/* -------------------------------------------------------
			リストクリックでジャンプ
		--------------------------------------------------------*/
		$('.mokuji li, .toc li').click(function(){
			var href = $(this).find('a').attr('href');
			var target = $(href == '#' || href == '' ? 'html' : href);
			var position = target.offset().top;
			$(window).scrollTop(position)
			return false;
		});
		
		/* -------------------------------------------------------
			カレント位置表示切替
		--------------------------------------------------------*/
		var secTopArr = new Array();
		secTopArr.length = 0;
		var current = -1;
	
		// 現在位置の取得
		$('article [id^="chapter"]').each(function(i){
			secTopArr[i] = $(this).offset().top;
		});

		//スクロールイベント
		$(window).on('load scroll',function(){
			for (var i = secTopArr.length-1; i>=0; i--) {
				if ($(window).scrollTop() > secTopArr[i] - 20) {
					$('.mokuji li').removeClass('current').eq(i).addClass('current');
					$('.mokuji ol ol li.current').parent('ol').prev().addClass('current');
					break;
				}
			}
		});
	}
	makeMokuji();
});

