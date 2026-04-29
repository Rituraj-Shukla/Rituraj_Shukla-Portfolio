import codecs

path = r'c:\Users\91639\Downloads\davies-mainfiles\davies\home.html'

with codecs.open(path, 'r', 'utf-8') as f:
    content = f.read()

index = content.find('<!-- AI Systems Pipeline Animation -->')
if index != -1:
    new_content = content[:index] + """<!-- AI Systems Pipeline Animation -->
    <style>
        /* Desktop Fixes */
        .desktop-connection-line {
            animation: desktopLineFlow 4.8s linear infinite !important;
            background-size: 200% 100% !important;
        }

        @keyframes desktopLineFlow {
            0% {
                background-position: 200% 0;
            }
            100% {
                background-position: -100% 0;
            }
        }

        /* Mobile Fixes */
        @media (max-width: 768px) {
            .mobile-progress-line {
                left: 15px !important;
                right: auto !important;
                transform-origin: top center !important;
            }
            
            .pipeline-arrow {
                transform: rotate(90deg) !important;
                margin: 10px auto !important;
                display: flex !important;
                justify-content: center !important;
            }
            
            .pipeline-arrow svg {
                transform: none !important;
            }
        }
    </style>
    <script>
        (function() {
            const AISystemsAnimation = {
                isMobile: false,
                blocks: [],
                lineElement: null,
                animationStartTime: null,
                animationDuration: 4800, // Sync with 4.8s CSS animation
                rafId: null,
                
                init() {
                    this.detectDevice();
                    this.setupElements();
                    this.isMobile ? this.initMobileScrollAnimation() : this.initDesktopAnimation();
                    window.addEventListener('resize', () => this.handleResize());
                },
                
                detectDevice() {
                    this.isMobile = window.innerWidth <= 768;
                },
                
                setupElements() {
                    const wrapper = document.getElementById('pipelineWrapper');
                    this.blocks = wrapper?.querySelectorAll('[data-pipeline-step]') || [];
                    this.lineElement = document.querySelector('.desktop-connection-line');
                },
                
                handleResize() {
                    const wasMobile = this.isMobile;
                    this.detectDevice();
                    if (wasMobile !== this.isMobile) {
                        if (this.rafId) {
                            cancelAnimationFrame(this.rafId);
                            this.rafId = null;
                        }
                        this.resetAnimation();
                        this.isMobile ? this.initMobileScrollAnimation() : this.initDesktopAnimation();
                    }
                },
                
                initDesktopAnimation() {
                    if (this.rafId) {
                        cancelAnimationFrame(this.rafId);
                        this.rafId = null;
                    }
                    this.animationStartTime = performance.now();
                    this.updateStepGlowByProgress(0);
                    this.trackLineProgress();
                },
                
                trackLineProgress() {
                    const animate = () => {
                        if (!this.isMobile) {
                            const elapsed = (performance.now() - this.animationStartTime) % this.animationDuration;
                            const progress = elapsed / this.animationDuration;
                            this.updateStepGlowByProgress(progress);
                            this.rafId = requestAnimationFrame(animate);
                        } else {
                            if (this.rafId) {
                                cancelAnimationFrame(this.rafId);
                                this.rafId = null;
                            }
                        }
                    };
                    this.rafId = requestAnimationFrame(animate);
                },
                
                updateStepGlowByProgress(progress) {
                    let activeStep = 0;
                    
                    if (progress < 0.2) activeStep = 1;
                    else if (progress < 0.4) activeStep = 2;
                    else if (progress < 0.6) activeStep = 3;
                    else if (progress < 0.8) activeStep = 4;
                    else activeStep = 5;
                    
                    this.blocks.forEach(block => block.classList.remove('step-active'));
                    
                    this.blocks.forEach(block => {
                        if (parseInt(block.dataset.pipelineStep) === activeStep) {
                            block.classList.add('step-active');
                        }
                    });
                },
                
                initMobileScrollAnimation() {
                    if (!('IntersectionObserver' in window)) return;
                    const observer = new IntersectionObserver((entries) => {
                        entries.forEach((entry) => {
                            if (entry.isIntersecting) {
                                entry.target.classList.add('step-visible');
                            } else {
                                entry.target.classList.remove('step-visible');
                            }
                        });
                    }, { threshold: 0.5 });
                    
                    this.blocks.forEach(block => observer.observe(block));
                    window.addEventListener('scroll', () => this.updateMobileProgress());
                },
                
                updateMobileProgress() {
                    const wrapper = document.getElementById('pipelineWrapper');
                    const progressLine = document.getElementById('mobileProgressLine');
                    if (!wrapper || !progressLine) return;
                    
                    const rect = wrapper.getBoundingClientRect();
                    const scrollTop = window.scrollY;
                    const wrapperTop = rect.top + scrollTop;
                    const wrapperHeight = rect.height;
                    const viewportHeight = window.innerHeight;
                    
                    const startPoint = wrapperTop - viewportHeight / 2;
                    const endPoint = wrapperTop + wrapperHeight;
                    const progress = Math.max(0, Math.min(1, (scrollTop - startPoint) / (endPoint - startPoint)));
                    progressLine.style.height = (progress * 100) + '%';
                },
                
                resetAnimation() {
                    this.blocks.forEach(block => block.classList.remove('step-active', 'step-visible'));
                }
            };
            
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', () => AISystemsAnimation.init());
            } else {
                AISystemsAnimation.init();
            }
        })();
    </script>
</body>
</html>"""
    with codecs.open(path, 'w', 'utf-8') as f:
        f.write(new_content)
    print("Success")
else:
    print("Not found")
