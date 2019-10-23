---
layout: post
title: Cross Correlation
date: 2019-10-21 09:41:24.000000000 +09:00
---

```matlab
% A demonstration of cross correlation in action.
% Hit the space bar during the demo to execute
% 
% https://dadorran.wordpress.com/2014/04/25/cross-correlation-demo/
clc;close all
a = [0.1 0.2  -0.1 4.1 -2 1.5 0 ];
b = [0.1 4 -2.2 1.6 0.1 0.1 0.2];
 
len = length(a);
if(len ~= length(b))
    error('vectors supplied must be the same length');
end
figure
set(gcf, 'position', [ 285   347   642   367]);
 
max_amp = max([max(a) max(b)]);
min_amp = min([min(a) min(b)]);
 
 
plot_h = 0.25;
text_h = 0.1;
ax1 = subplot(2,1,1);
pl1_line = plot(a);
labels1 = text([1:len], a , num2str(a'), 'VerticalAlignment','bottom', ...
                             'HorizontalAlignment','right','fontsize',8);
hold on; pl1_dot = plot(a,'r.');
xlim([1 len])
ylim([min_amp max_amp])
 
set(ax1,'position', [(1/3) 0.95-plot_h (1/3) plot_h])
set(ax1,'visible','off')
 
ax2 = subplot(2,1,2);
pl2_line = plot(b);
labels2 = text([1:len], b , num2str(b'), 'VerticalAlignment','bottom', ...
                             'HorizontalAlignment','right','fontsize',8);
hold on; pl2_dot = plot(b,'r.');
xlim([1 len])
ylim([min_amp max_amp])
set(ax2,'visible','off')
set(ax2,'position', [(1/3) 0.9-plot_h*2 (1/3) plot_h])
 
 
str = '';
for k = 1: len
    str = [str '(' num2str(a(k)) ')(' num2str(b(k)) ') + '];
end
str(end-1)  = '=';
str = [str num2str(sum(a.*b))];
r_ba = xcorr(a,b);
 
corr_calc_text = annotation('textbox',  [0 0.85-plot_h*2-text_h 1 text_h], 'linestyle','none','horizontalalignment','center' ,'string', {'correlation at zero lag is ' str}, 'fontsize', 8);
 
annotation('textbox',  [0.5 0.8-plot_h*2-text_h*2 1 text_h], 'linestyle','none','horizontalalignment','left' ,'string', sprintf('%.2f',r_ba(len)),'color','red', 'fontsize', 8);
 
 
pause
 
x_inc= (1/3)/(len-1);
for k = 1:len-1
 
    str = '';
    for m = 1: len-k
        str = [str '(' num2str(a(m+k)) ')(' num2str(b(m)) ') + '];
    end
    str(end-1)  = '=';
    str = [str num2str(r_ba(len+k))];
 
    set(corr_calc_text,'string', {['correlation at lag of ' num2str(k) ' is '] str}, 'fontsize', 8);
     
    set(ax2,'position', [(1/3)+k*x_inc 0.9-plot_h*2 (1/3) plot_h])
     
    annotation('textbox',  [0.5+x_inc*k 0.8-plot_h*2-text_h*2 1 text_h], 'linestyle','none','horizontalalignment','left' ,'string', sprintf('%.2f',r_ba(len+k)),'color','red', 'fontsize', 8);
    if(k ==1)
        pause
        annotation('textbox',  [0.5 0.01 1 text_h], 'linestyle','none','horizontalalignment','left' ,'string', ['   0'] ,'color','blue', 'fontsize', 8);
        annotation('textbox',  [0.001 0.01 1 text_h], 'linestyle','none','horizontalalignment','left' ,'string', ['Lag:'] ,'color','blue');
        annotation('textbox',  [0.5+x_inc*(len) 0.8-plot_h*2-text_h*2 1 text_h], 'linestyle','none','horizontalalignment','left' ,'string', ']' ,'color','red');
        annotation('textbox',  [0.5-x_inc*(len-1)-x_inc/2 0.8-plot_h*2-text_h*2 1 text_h], 'linestyle','none','horizontalalignment','left' ,'string', '[' ,'color','red');
        annotation('textbox',  [0.001 0.8-plot_h*2-text_h*2 1 text_h], 'linestyle','none','verticalalignment','middle','horizontalalignment','left' ,'string', {'Correlation' 'Sequence:'} ,'color','red');
 
    end
    annotation('textbox',  [0.5+x_inc*k 0.01 1 text_h], 'linestyle','none','horizontalalignment','left' ,'string', ['   ' num2str(k)] ,'color','blue', 'fontsize', 8);
 
    pause
end
 
for k = 1:len-1
 
    str = '';
    for m = 1: len-k
        str = [str '(' num2str(a(m)) ')(' num2str(b(m+k)) ') + '];
    end
    str(end-1)  = '=';
    str = [str num2str(r_ba(len-k))];
 
    set(corr_calc_text,'string', {['correlation at lag of ' num2str(-1*k) ' is '] str}, 'fontsize', 8);
     
    set(ax2,'position', [(1/3)-k*x_inc 0.9-plot_h*2 (1/3) plot_h])
    annotation('textbox',  [0.5-x_inc*k 0.8-plot_h*2-text_h*2 1 text_h], 'linestyle','none','horizontalalignment','left' ,'string', sprintf('%.2f',r_ba(len-k)),'color','red', 'fontsize', 8);
    annotation('textbox',  [0.5-x_inc*k 0.01 1 text_h], 'linestyle','none','horizontalalignment','left' ,'string', ['   ' num2str(k*-1)] ,'color','blue', 'fontsize', 8);
 
    pause
end
 
% Uncomment the next two lines if you would like to see a plot of the
% correlation sequence
% [corr_seq lags] =  xcorr(a,b);
% plot(lags,corr_seq)
% xlabel('lags');ylabel('correlation measure');
```
