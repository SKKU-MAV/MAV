# # readline_test.py
# f = open("C:/doit/새파일.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

li = ["권성우","김대원","김도현","김동현","김준서","김준서","김지운","김태민","김태환","김현중","류나정","류성희","병철","신채훈","심윤보","원태연","이근서","이용하","이재혁","이지현","전수연","정일원","정주은","정주희","정철주","채서영","한주원","홍여원","황준원"]
li1 = ["유지훈", "이용하", "홍승연", "최선아"]
li2 = ["이다연", "김민성", "박정휴", "강동윤", "김혜준", "김서현", "박준명", "김진규", "박지연", "김채리", "박훈영", "이태권", "김윤정", "오치헌", "송현준", "강태영", "이시현", "김진욱", "강현서"]
li.sort
li2.sort
data =""
for i in li2:
  # print(
  #   '''
  #         <li>
  #           <img src="./images/github-mark.png" alt="''' +
  #           i,
  #           '''사진" />
  #           <div class="item-content">
  #             <div>
  #               <h2>'''+
  #               i+ '''</h2>
  #               <p>
  #                 한 줄 소개란
  #               </p>
  #               <div class="actions">
  #                 <a href="https://github.com/" aria-label="Homepage" class="footer-octicon" title="GitHub">
  #                   <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
  #                   </svg>
  #                 </a>
  #               </div>
  #             </div>
  #           </div>
  #         </li>'''
  # )

  print(
    '''
            <li class="card-item">
              <article>
                <img src="./images/github-mark.png" alt="'''+i+'''" />
                <div class="card-item-content">
                  <h2>'''+i+'''</h2>
                  <a href="https://github.com/" aria-label="Homepage" class="footer-octicon" title="GitHub">
                    <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                    </svg>
                  </a>
                </div>
              </article>
            </li>'''
  )     

