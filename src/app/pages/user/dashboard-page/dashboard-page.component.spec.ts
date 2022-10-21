import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DashboardPageComponent } from '~/app/pages/admin/dashboard-page/dashboard-page.component';
import { UserPagesModule } from '~/app/pages/user/user-pages.module';
import { RgwService } from '~/app/shared/services/api/rgw.service';
import { TestingModule } from '~/app/testing.module';

describe('DashboardPageComponent', () => {
  let component: DashboardPageComponent;
  let fixture: ComponentFixture<DashboardPageComponent>;
  let rgwService: RgwService;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [DashboardPageComponent],
      imports: [UserPagesModule, TestingModule]
    }).compileComponents();
  });

  beforeEach(() => {
    rgwService = TestBed.inject(RgwService);
    // @ts-ignore
    jest.spyOn(rgwService, 'buildHeaders').mockReturnValue({});
    fixture = TestBed.createComponent(DashboardPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
